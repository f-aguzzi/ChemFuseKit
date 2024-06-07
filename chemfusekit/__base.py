'''A base class for all classifiers.'''

import pandas as pd
import numpy as np
import joblib

from sklearn.base import BaseEstimator

from .__utils import GraphMode


class BaseDataModel:
    '''Models the output data from data-outputting operations'''

    def __init__(self, x_data: pd.DataFrame, x_train: pd.DataFrame, y: np.ndarray):
        self.x_data = x_data
        self.x_train = x_train
        self.y = y

    @classmethod
    def load_from_file(cls, import_path: str, sheet_name: str = 'Sheet1'):
        try:
            table_data = pd.read_excel(
                import_path,
                sheet_name=sheet_name,
                index_col=0,
                header=0
            )
        except Exception as exc:
            raise FileNotFoundError("Error opening the selected files.") from exc

        x = table_data.iloc[:, 1:]

        # It is necessary to convert the column names as string to select them
        x.columns = x.columns.astype(str)  # to make the colnames as text

        y = table_data.loc[:, 'Substance'].values
        y_dataframe = pd.DataFrame(y, columns=['Substance'])
        x_train = pd.concat(
            [y_dataframe, x],
            axis=1
        )

        return cls(x, x_train, y)

    def export_to_file(self, export_path: str, sheet_name: str = 'Sheet1'):
        try:
            self.x_train.to_excel(excel_writer=export_path, sheet_name=sheet_name)
        except Exception as exc:
            raise RuntimeError("Could not export data to the selected path.") from exc


class BaseSettings:
    '''Holds the settings for the BaseClassifier object.'''

    def __init__(self, output: GraphMode = GraphMode.NONE, test_split: bool = False):
        if test_split is True and output is GraphMode.NONE:
            raise Warning(
                "You selected test_split but it won't run because you disabled the output."
            )
        self.output = output
        self.test_split = test_split


class BaseClassifier:
    '''Parent class for all classifiers, containing basic shared utilities.'''

    def __init__(self, settings: BaseSettings, data: BaseDataModel):
        self.settings = settings
        self.data = data
        self.model: BaseEstimator | None = None

    def import_model(self, import_path: str):
        model = joblib.load(import_path)
        if not isinstance(model, BaseEstimator):
            raise ImportError("The file you tried importing is not a sklearn model!")
        self.model = model

    def export_model(self, export_path: str):
        if self.model is not None:
            joblib.dump(self.model, export_path)
        else:
            raise RuntimeError("You haven't trained the model yet! You cannot export it now.")

    def predict(self, x_data: pd.DataFrame):
        '''Performs prediction once the model is trained.'''
        if x_data is None:
            raise TypeError(f"X data for {self.__class__.__name__} prediction must be non-empty.")
        if self.model is None:
            raise RuntimeError(f"The {self.__class__.__name__} model is not trained yet!")

        y_pred = self.model.predict(x_data)
        return y_pred
