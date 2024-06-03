'''Performs low-level data fusion on input arrays, outputs the results'''
from typing import Optional, List

import numpy as np
import pandas as pd
from scipy.signal import savgol_filter

from .__utils import GraphMode


class Table:
    '''Holds the path, preprocessing choice and sheet name for a single Excel table.'''
    def __init__(self, file_path: str, sheet_name: str, preprocessing: str):
        self.file_path = file_path
        self.sheet_name = sheet_name
        self.preprocessing = preprocessing


class LLDFModel:
    '''Models the output data from the LLDF operation'''
    def __init__(self, x_data: pd.DataFrame, x_train: pd.DataFrame, y: np.ndarray):
        self.x_data = x_data
        self.x_train = x_train
        self.y = y


class LLDFSettings:
    '''Holds the settings for the LLDF object.'''
    def __init__(self, output: GraphMode = GraphMode.NONE):
        self.output = output


def _snv(input_data: np.ndarray):
    '''Applies normalization to an input array'''
    # Define a new array and populate it with the corrected data
    output_data = np.zeros_like(input_data)
    for i in range(input_data.shape[0]):

        # Apply correction
        output_data[i,:] = (
            (input_data[i,:] - np.mean(input_data[i,:])) / np.std(input_data[i,:])
        )

    return output_data


class LLDF:
    '''Holds together all the data, methods and artifacts of the LLDF operation'''
    def __init__(self, tables: List[Table], settings: LLDFSettings):
        self.settings = settings
        self.tables = tables
        self.fused_data: Optional[LLDFModel] = None

    def lldf(self):
        '''Performs low-level data fusion'''
        x_vector = []
        for table in self.tables:
            try:
                table_data = pd.read_excel(
                    table.file_path,
                    sheet_name=table.sheet_name,
                    index_col=0,
                    header=0
                )
            except Exception as exc:
                raise FileNotFoundError("Error opening the selected files.") from exc

            # select only numerical attributes
            x = table_data.iloc[:, 1:]

            # It is necessary to convert the column names as string to select them
            x.columns = x.columns.astype(str)     # to make the colnames as text

            # Preprocessing
            if table.preprocessing == 'snv':
                # Compute the SNV on spectra
                preprocessed_x = _snv(x.values)
            elif table.preprocessing == 'savgol':
                # Preprocessing with Savitzki-Golay
                # smoothing, defining the window, the order and the use of derivatives
                preprocessed_x = savgol_filter(x, 7, polyorder=2, deriv=0)
            elif table.preprocessing == 'savgol+snv':
                # We can also combine the preprocessing strategies together:
                # Savitzki-Golay - smoothing + SNV
                preprocessed_x = _snv(savgol_filter(x, 7, polyorder=2, deriv=0))
            elif table.preprocessing == 'none':
                # Skip preprocessing
                preprocessed_x = x
            else:
                raise SyntaxError(
                    f"LLDF: this type of preprocessing does not exist ({table.preprocessing=})"
                )

            # Create a new DataFrame with the processed numerical attributes
            processed_dataframe_x = pd.DataFrame(
                preprocessed_x,
                columns=x.columns
            )

            x_vector.append(x)

        try:
            table_data = pd.read_excel(
                self.tables[0].file_path,
                sheet_name=self.tables[0].sheet_name,
                index_col=0,
                header=0
            )
        except Exception as exc:
            raise FileNotFoundError("Error opening the selected files.") from exc

        y = table_data.loc[:, 'Substance'].values
        y_dataframe = pd.DataFrame(y, columns=['Substance'])

        # Fused dataset
        x_data = pd.concat(
            x_vector,
            axis=1
        )

        # X training set
        x_train = pd.concat(
            [y_dataframe, x_data],
            axis=1
        )

        self.fused_data = LLDFModel(x_data, x_train, y)

    def export_data(self, export_path: str):
        '''Exports the data fusion artifacts to a file'''
        if self.fused_data is None:
            raise RuntimeError("Cannot export data before data fusion.")

        x_train_dataframe = pd.DataFrame(self.fused_data.x_train)

        try:
            x_train_dataframe.to_excel(export_path)
        except Exception as exc:
            raise RuntimeError("Could not export data to the selected path.") from exc
