"""Performs low-level data fusion on input arrays, outputs the results"""
from typing import Optional, List

import numpy as np
import pandas as pd
from scipy.signal import savgol_filter

import matplotlib.pyplot as plt

from .__base import BaseDataModel, BaseSettings
from .__utils import GraphMode
from .pca import PCASettings, PCA
from .plsda import PLSDASettings, PLSDA


class Table:
    """Holds the path, preprocessing choice and sheet name for a single Excel table."""

    def __init__(self, file_path: str, sheet_name: str, preprocessing: str, feature_selection: str | None = None,
                 class_column: str = 'Substance', index_column: str | None = None):
        self.file_path = file_path
        self.sheet_name = sheet_name
        self.preprocessing = preprocessing
        self.feature_selection = feature_selection
        self.class_column = class_column
        self.index_column = index_column


class DFDataModel(BaseDataModel):
    """Models the output data from the DF operation"""

    def __init__(self, x_data: pd.DataFrame, x_train: pd.DataFrame, y: np.ndarray,
                 tables: list[tuple[Table, BaseDataModel]]):
        super().__init__(x_data, x_train, y)
        self.tables = tables


class DFSettings(BaseSettings):
    """Holds the settings for the DF object."""

    def __init__(self, output: str = 'none', method: str = 'concat'):
        super().__init__(output)
        if method not in ['concat', 'outer']:
            raise ValueError("DF: invalid method: must be 'concat' or 'outer'")
        self.method = method


def _snv(input_data: np.ndarray):
    """Applies normalization to an input array"""
    # Define a new array and populate it with the corrected data
    output_data = np.zeros_like(input_data)
    for i in range(input_data.shape[0]):
        # Apply correction
        output_data[i, :] = (
                (input_data[i, :] - np.mean(input_data[i, :])) / np.std(input_data[i, :])
        )

    return output_data


class DF:
    """Holds together all the data, methods and artifacts of the LLDF operation"""

    def __init__(self, settings: DFSettings, tables: List[Table]):
        self.settings = settings
        self.tables = tables
        self.fused_data: Optional[DFDataModel] = None

    def fuse(self):
        """Performs data fusion"""
        x_vector = []
        individual_tables = []
        for table in self.tables:
            table_data = self._import_table(table.file_path, table.sheet_name)

            # select only numerical attributes
            if table.index_column is not None and table.index_column in table_data.columns:
                deindexed_table = table_data.drop(table.index_column, axis=1)
            else:
                deindexed_table = table_data

            if table.class_column in table_data.columns:
                x = deindexed_table.drop(table.class_column, axis=1)
                y = deindexed_table[table.class_column]
            else:
                x = deindexed_table.iloc[:, 1:]
                y = deindexed_table.iloc[:, 0]

            # It is necessary to convert the column names as string to select them
            x.columns = x.columns.astype(str)  # to make the colnames as text

            try:
                preprocessed_x = self._preprocess_table(table, x)
            except Warning as w:
                preprocessed_x = x

            # Rename the class column to 'Substance'
            y.columns = ['Substance']
            preprocessed_x = pd.DataFrame(preprocessed_x, columns=x.columns)

            # Reset table indices to prevent misalignment during concatenation
            preprocessed_x.reset_index(drop=True, inplace=True)
            y.reset_index(drop=True, inplace=True)

            # Save the temporary table as a BaseDataModel
            x_train = pd.concat([y, preprocessed_x], axis=1)
            x_train.reset_index(drop=True, inplace=True)
            table_data_model = BaseDataModel(
                x_data=preprocessed_x,
                x_train=x_train,
                y=np.asarray(y)
            )

            # Feature reduction
            if table.feature_selection is None:
                reduced_table_data_model = table_data_model
            else:
                reduced_table_data_model = self._perform_feature_selection(table, table_data_model)

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
                    if table.file_path.endswith('.xlsx'):
                        fig.suptitle(f'Imported table: {table.sheet_name} from {table.file_path}')
                    else:
                        fig.suptitle(f'Imported table: {table.file_path}')
                else:
                    # Let's plot the different datasets we preprocessed
                    fig, ax1 = plt.subplots(1, figsize=(15, 15))
                    if x.shape[1] == 1:
                        ax1.plot(x)
                    else:
                        ax1.plot(wl, x.T)
                    if table.file_path.endswith('.xlsx'):
                        fig.suptitle(f'Imported table: {table.sheet_name} from {table.file_path} (no preprocessing)')
                    else:
                        fig.suptitle(f'Imported table: {table.file_path} (no preprocessing)')

            # Create a new DataFrame with the processed numerical attributes
            processed_dataframe_x = pd.DataFrame(
                reduced_table_data_model.x_data,
                columns=reduced_table_data_model.x_data.columns
            )

            # Reset the index of the dataframe to avoid misalignment during concatenation
            processed_dataframe_x = processed_dataframe_x.reset_index(drop=True)

            x_vector.append(processed_dataframe_x)
            individual_tables.append((table, reduced_table_data_model))

        y = individual_tables[0][1].y
        y_dataframe = pd.DataFrame(y, columns=['Substance'])

        # Fused dataset
        # Concatenation - based approach
        if self.settings.method == 'concat' or len(x_vector) <= 1:
            x_data = pd.concat(
                x_vector,
                axis=1
            )
        # Matrix multiplication - based approach
        else:
            x_data = x_vector[0]
            for matrix in x_vector[1:]:
                outer_product = np.einsum('ij,ik->ijk', x_data, matrix)
                x_data = np.sum(outer_product, axis=2)
            x_data = pd.DataFrame(x_data, columns=x_vector[0].columns)

        # X training set
        x_train = pd.concat(
            [y_dataframe, x_data],
            axis=1
        )

        self.fused_data = DFDataModel(x_data, x_train, y, individual_tables)

    @staticmethod
    def _preprocess_table(table, x):
        if x.shape[1] == 1 and table.preprocessing != 'none':
            raise Warning("The array is 1-dimensional, therefore it cannot be preprocessed.")
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
                f"DF: this type of preprocessing does not exist ({table.preprocessing=})"
            )
        return preprocessed_x

    @staticmethod
    def _perform_feature_selection(table: Table, data_model: BaseDataModel) -> BaseDataModel:
        """Performs feature selection on a table"""
        if table.feature_selection == 'pca':
            pca = PCA(PCASettings(), data_model)
            pca.train()
            return pca.rescaled_data
        elif table.feature_selection == 'plsda':
            plsda = PLSDA(PLSDASettings(), data_model)
            plsda.train()
            return plsda.rescaled_data
        else:
            raise SyntaxError(
                f"DF: this type of feature selection does not exist ({table.feature_selection=})"
            )

    @staticmethod
    def _import_table(file_path, sheet_name) -> pd.DataFrame:
        """Imports a table from a file"""
        try:
            # Autodetect the format based on the file extension
            if file_path.endswith('.xlsx'):
                table_data = pd.read_excel(
                    file_path,
                    sheet_name=sheet_name,
                    index_col=0,
                    header=0
                )
            elif file_path.endswith('.csv'):
                table_data = pd.read_csv(
                    file_path,
                    index_col=0,
                    header=0
                )
            elif file_path.endswith('.json'):
                table_data = pd.read_json(
                    file_path,
                    orient='table'  # or other orientations based on your json format
                )
            else:
                raise ValueError(f"Unsupported file format: {file_path}")
        except Exception as exc:
            raise FileNotFoundError("Error opening the selected files.") from exc

        return table_data

    def export_data(self, export_path: str, sheet_name: str = 'Sheet1'):
        """Exports the data fusion artifacts to a file"""
        if self.fused_data is None:
            raise RuntimeError("Cannot export data before data fusion.")

        self.fused_data.export_to_file(export_path=export_path, sheet_name=sheet_name)
