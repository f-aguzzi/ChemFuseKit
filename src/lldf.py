'''Performs low-level data fusion on input arrays, outputs the results'''
import numpy as np
import pandas as pd
from scipy.signal import savgol_filter

# COSE DA FARE: SCELTA PREPROCESSING, TESTARE EXPORT

class LLDFModel:
    '''Models the output data from the LLDF operation'''
    def __init__(self, x_data, y_dataframe, x_train, y):
        self.x_data = x_data
        self.x_dataframe = y_dataframe
        self.x_train = x_train
        self.y = y

class LLDF:
    '''Holds together all the data, methods and artifacts of the LLDF operation'''
    def __init__(self, preprocessing='snv'):
        self.preprocessing = preprocessing
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
        path = input("Insert the QEPAS file path:")
        sheet = input("Insert the QEPAS sheet name:")
        spectra = pd.read_excel(path, sheet_name=sheet, index_col=0, header=0)
        path = input("Insert the GC file path:")
        sheet = input("Insert the GC sheet name:")
        ret_time = pd.read_excel(path, sheet_name=sheet, index_col=0, header=0)

        # select only numerical attributes
        x_spectra = spectra.iloc[:, 1:]
        x_time = ret_time.iloc[:, 1:]

        #Selection of classes from the spectra database
        y = spectra.loc[:, 'Substance'].values

        y_dataframe = pd.DataFrame(y, columns=['Substance'])

        # It is necessary to convert the column names as string to select them
        spectra.columns = spectra.columns.astype(str) # to make the colnames as text

        # Preprocessing
        if self.preprocessing == 'snv':
            # Compute the SNV on spectra
            preprocessed_spectra = self._snv(x_spectra.values)
        elif self.preprocessing == 'savgol':
            # Preprocessing with Savitzki-Golay
            # smoothing, defining the window, the order and the use of derivatives
            preprocessed_spectra = savgol_filter(x_spectra, 7, polyorder = 2, deriv=0)
        elif self.preprocessing == 'savgol+snv':
            # We can also combine the preprocessing strategies together:
            # Savitzki-Golay - smoothing + SNV
            preprocessed_spectra = self._snv(savgol_filter(x_spectra, 7, polyorder = 2, deriv=0))
        else:
            raise Exception(
                f"LLDF: this type of preprocessing does not exist ({self.preprocessing=})"
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

        self.fused_data = LLDFModel(x_data, y_dataframe, x_train, y)

    def export_data(self):
        '''Exports the data fusion artifacts to a file'''
        path = input("Insert the output file path: ")
        pd.DataFrame(self.fused_data).to_excel(path)
