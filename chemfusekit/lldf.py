'''Performs low-level data fusion on input arrays, outputs the results'''
from typing import Optional, List

import numpy as np
import pandas as pd
from scipy.signal import savgol_filter

import matplotlib
import matplotlib.pyplot as plt

from .__base import GraphMode, BaseDataModel


class Table:
    '''Holds the path, preprocessing choice and sheet name for a single Excel table.'''
    def __init__(self, file_path: str, sheet_name: str, preprocessing: str, class_column: str = 'Substance',
                 index_column: str | None = None):
        self.file_path = file_path
        self.sheet_name = sheet_name
        self.preprocessing = preprocessing
        self.class_column = class_column
        self.index_column = index_column


class LLDFDataModel(BaseDataModel):
    '''Models the output data from the LLDF operation'''
    def __init__(self, x_data: pd.DataFrame, x_train: pd.DataFrame, y: np.ndarray):
        super().__init__(x_data, x_train, y)


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
        output_data[i, :] = (
            (input_data[i, :] - np.mean(input_data[i,:])) / np.std(input_data[i, :])
        )

    return output_data


class LLDF:
    '''Holds together all the data, methods and artifacts of the LLDF operation'''
    def __init__(self, settings: LLDFSettings, tables: List[Table]):
        self.settings = settings
        self.tables = tables
        self.fused_data: Optional[LLDFDataModel] = None

    def lldf(self):
        '''Performs low-level data fusion'''
        x_vector = []
        for table in self.tables:
            try:
                # Autodetect the format based on the file extension
                if table.file_path.endswith('.xlsx'):
                    table_data = pd.read_excel(
                        table.file_path,
                        sheet_name=table.sheet_name,
                        index_col=0,
                        header=0
                    )
                elif table.file_path.endswith('.csv'):
                    table_data = pd.read_csv(
                        table.file_path,
                        index_col=0,
                        header=0
                    )
                elif table.file_path.endswith('.json'):
                    table_data = pd.read_json(
                        table.file_path,
                        orient='table'  # or other orientations based on your json format
                    )
                else:
                    raise ValueError(f"Unsupported file format: {table.file_path}")
            except Exception as exc:
                raise FileNotFoundError("Error opening the selected files.") from exc

            # select only numerical attributes
            if table.index_column is not None and table.index_column in table_data.columns:
                x = table_data.drop(table.index_column, axis=1)
            else:
                x = table_data.iloc[:, 1:]

            if table.class_column in table_data.columns:
                x = table_data.drop(table.class_column, axis=1)
            else:
                x = x.iloc[:, 1:]

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

            if self.settings.output is GraphMode.GRAPHIC:
                numbers_string = [str(col) for col in x.columns]

                # Replace commas with points and join the numbers with a space
                try:
                    wl = np.array(list(map(lambda z: float(z.replace(',', '.')), numbers_string)))
                except ValueError:
                    wl = numbers_string

                if table.preprocessing != 'none':
                    # Let's plot the different datasets we preprocessed
                    fig, (ax1, ax2) = plt.subplots(2, figsize=(15, 15))
                    ax1.plot(wl, x.T)
                    ax1.set_title(f'Original data')
                    ax2.plot(wl, preprocessed_x.T)
                    ax2.set_title(f'Processed table with {table.preprocessing}')
                    fig.suptitle(f'Imported table: {table.file_path}')
                else:
                    # Let's plot the different datasets we preprocessed
                    fig, ax1 = plt.subplots(1, figsize=(15, 15))
                    ax1.plot(wl, x.T)
                    fig.suptitle(f'Imported table: {table.file_path} (no preprocessing)')

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

        y = table_data.loc[:, self.tables[0].class_column].values
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

        self.fused_data = LLDFDataModel(x_data, x_train, y)

    def export_data(self, export_path: str, sheet_name: str = 'Sheet1'):
        '''Exports the data fusion artifacts to a file'''
        if self.fused_data is None:
            raise RuntimeError("Cannot export data before data fusion.")

        self.fused_data.export_to_file(export_path=export_path, sheet_name=sheet_name)
