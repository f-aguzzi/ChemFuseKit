'''Performs low-level data fusion on input arrays, outputs the results'''
import numpy as np
import pandas as pd
from scipy.signal import savgol_filter

# COSE DA FARE: SCELTA PREPROCESSING, TESTARE EXPORT

class LLDFModel:
    '''Models the output data from the LLDF operation'''
    def __init__(self, x_data, x_train, y):
        self.x_data = x_data
        self.x_train = x_train
        self.y = y

class LLDFSettings:
    '''Holds the settings for the LLDF object.'''
    def __init__(self, qepas_path, qepas_sheet, rt_path, rt_sheet, preprocessing='snv'):
        self.qepas_path = qepas_path
        self.qepas_sheet = qepas_sheet
        self.rt_path = rt_path
        self.rt_sheet = rt_sheet
        self.preprocessing = preprocessing

class LLDF:
    '''Holds together all the data, methods and artifacts of the LLDF operation'''
    def __init__(self, settings):
        self.settings = settings
        self.fused_data = None

    def _snv(self, input_data):
        '''Applies normalization to an input array'''
        # Define a new array and populate it with the corrected data
        output_data = np.zeros_like(input_data)
        for i in range(input_data.shape[0]):

            # Apply correction
            output_data[i,:] = (
                (input_data[i,:] - np.mean(input_data[i,:])) / np.std(input_data[i,:])
            )

        return output_data

    def lldf(self):
        '''Performs low-level data fusion'''
        try:
            spectra = pd.read_excel(
                self.settings.qepas_path,
                sheet_name=self.settings.qepas_sheet,
                index_col=0,
                header=0
            )

            ret_time = pd.read_excel(
                self.settings.rt_path,
                sheet_name=self.settings.rt_sheet,
                index_col=0,
                header=0
            )
        except Exception as exc:
            raise FileNotFoundError("Error opening the selected files.") from exc

        # select only numerical attributes
        x_spectra = spectra.iloc[:, 1:]
        x_time = ret_time.iloc[:, 1:]

        #Selection of classes from the spectra database
        y = spectra.loc[:, 'Substance'].values

        y_dataframe = pd.DataFrame(y, columns=['Substance'])

        # It is necessary to convert the column names as string to select them
        spectra.columns = spectra.columns.astype(str) # to make the colnames as text

        # Preprocessing
        if self.settings.preprocessing == 'snv':
            # Compute the SNV on spectra
            preprocessed_spectra = self._snv(x_spectra.values)
        elif self.settings.preprocessing == 'savgol':
            # Preprocessing with Savitzki-Golay
            # smoothing, defining the window, the order and the use of derivatives
            preprocessed_spectra = savgol_filter(x_spectra, 7, polyorder = 2, deriv=0)
        elif self.settings.preprocessing == 'savgol+snv':
            # We can also combine the preprocessing strategies together:
            # Savitzki-Golay - smoothing + SNV
            preprocessed_spectra = self._snv(savgol_filter(x_spectra, 7, polyorder = 2, deriv=0))
        else:
            raise SyntaxError(
                f"LLDF: this type of preprocessing does not exist ({self.settings.preprocessing=})"
            )


        # Create a new DataFrame with the processed numerical attributes
        processed_dataframe_spectra = pd.DataFrame(
            preprocessed_spectra,
            columns=spectra.columns[1:]
        )

        # Create a new DataFrame with the processed numerical attributes
        processed_dataframe_rt = pd.DataFrame(x_time.values, columns=ret_time.columns[1:])

        # X training set
        x_train = pd.concat(
            [y_dataframe, processed_dataframe_spectra, processed_dataframe_rt],
            axis = 1
        )

        # select only numerical attributes
        x_data = x_train.iloc[:, 1:]

        self.fused_data = LLDFModel(x_data, x_train, y)

    def export_data(self, export_path):
        '''Exports the data fusion artifacts to a file'''
        if self.fused_data is None:
            raise RuntimeError("Cannot export data before data fusion.")

        x_dataframe = pd.DataFrame(self.fused_data.x_data)
        x_train_dataframe = pd.DataFrame(self.fused_data.x_train)
        y_dataframe = pd.DataFrame(self.fused_data.y)

        try:
            pd.concat([x_train_dataframe, y_dataframe, x_dataframe], axis=1).to_excel(export_path)
        except Exception as exc:
            raise RuntimeError("Could not export data to the selected path.") from exc
