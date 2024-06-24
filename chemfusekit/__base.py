"""A base class for all classifiers."""
from abc import ABC, abstractmethod
from typing import Optional

import pandas as pd
import numpy as np
import joblib

from sklearn.base import BaseEstimator

from .__utils import GraphMode


class BaseDataModel:
    """Models the output data from data-outputting operations"""

    def __init__(self, x_data: pd.DataFrame, x_train: pd.DataFrame, y: np.ndarray):
        self.x_data = x_data
        self.x_train = x_train
        self.y = y

    @classmethod
    def load_from_file(cls, import_path: str, sheet_name: str = 'Sheet1', class_column: str = 'Substance',
                       index_column: str | None = None):
        try:
            # Autodetect the format based on the file extension
            if import_path.endswith('.xlsx'):
                table_data = pd.read_excel(
                    import_path,
                    sheet_name=sheet_name,
                    index_col=0,
                    header=0
                )
            elif import_path.endswith('.csv'):
                table_data = pd.read_csv(
                    import_path,
                    index_col=0,
                    header=0
                )
            elif import_path.endswith('.json'):
                table_data = pd.read_json(
                    import_path,
                    orient='table'  # or other orientations based on your json format
                )
            else:
                raise ValueError(f"Unsupported file format: {import_path}")
        except Exception as exc:
            raise FileNotFoundError("Error opening the selected files.") from exc

        if index_column is not None:
            x = table_data.drop(index_column, axis=1)
        else:
            x = table_data

        # It is necessary to convert the column names as string to select them
        x.columns = x.columns.astype(str)  # to make the colnames as text

        # Reset the index of the dataframe
        # x = x.reset_index(drop=True)

        y = table_data.loc[:, class_column].values
        x_train = x
        x_data = x_train.drop(class_column, axis=1)

        return cls(x_data, x_train, y)

    def export_to_file(self, export_path: str, sheet_name: str = 'Sheet1'):
        # Determine the file format based on the file extension
        if export_path.endswith('.xlsx'):
            try:
                self.x_train.to_excel(excel_writer=export_path, sheet_name=sheet_name)
            except Exception as exc:
                raise RuntimeError("Could not export data to the selected path.") from exc
        elif export_path.endswith('.csv'):
            try:
                self.x_train.to_csv(export_path, index=False)
            except Exception as exc:
                raise RuntimeError("Could not export data to the selected path.") from exc
        elif export_path.endswith('.json'):
            try:
                self.x_train.to_json(export_path, orient='table')  # or other orientations based on your needs
            except Exception as exc:
                raise RuntimeError("Could not export data to the selected path.") from exc
        else:
            raise ValueError(f"Unsupported file format: {export_path}")

    def __getitem__(self, index):
        """Get an item with array-style indexing"""
        return pd.DataFrame(self.x_data.iloc[index, :]).transpose()


class BaseSettings:
    """Holds the settings for all objects with settings."""

    def __init__(self, output: str = 'none'):
        if output == 'none':
            self.output = GraphMode.NONE
        elif output == 'graphical':
            self.output = GraphMode.GRAPHIC
        elif output == 'text':
            self.output = GraphMode.TEXT
        else:
            raise ValueError("The output mode should be 'none', 'graphical' or 'text'.")


class BaseActionClass(ABC):
    """Abstract base class for all reducers and classifiers."""
    def __init__(self, settings: BaseSettings, data: BaseDataModel):
        self.settings = settings
        self.data = data
        self.model: BaseEstimator | None = None

    @abstractmethod
    def train(self):
        """Trains the estimator model."""
        pass

    @classmethod
    def from_file(cls, settings, model_path):
        """Creates a classifier instance from file"""
        x_data = pd.DataFrame()
        y_dataframe = pd.DataFrame(columns=['Substance'])
        x_train = pd.concat([y_dataframe, x_data], axis=1)
        y = np.asarray(y_dataframe)
        data = BaseDataModel(
            x_data=x_data,
            x_train=x_train,
            y=y
        )
        class_instance = cls(settings, data)
        class_instance.import_model(model_path)
        return class_instance
    
    def import_model(self, import_path: str):
        """Imports a sklearn model from a file."""
        try:
            model = joblib.load(import_path)
        except Exception as exc:
            raise ImportError("The file you tried importing is not a valid Python object!") from exc
        if not isinstance(model, BaseEstimator):
            raise ImportError("The file you tried importing is not a sklearn model!")
        self.model = model

    def export_model(self, export_path: str):
        """Exports the underlying sklearn model to a file."""
        if self.model is not None:
            joblib.dump(self.model, export_path)
        else:
            raise RuntimeError("You haven't trained the model yet! You cannot export it now.")


class BaseClassifierSettings(BaseSettings):
    """Holds the settings for the BaseClassifier object."""

    def __init__(self, output: str = 'none', test_split: bool = False):
        super().__init__(output)
        if test_split is True and self.output is GraphMode.NONE:
            raise Warning(
                "You selected test_split but it won't run because you disabled the output."
            )
        self.test_split = test_split


class BaseClassifier(BaseActionClass, ABC):
    """Parent class for all classifiers, containing basic shared utilities."""

    def __init__(self, settings: BaseClassifierSettings, data: BaseDataModel):
        super().__init__(settings, data)

    def predict(self, x_data: pd.DataFrame):
        """Performs prediction once the model is trained."""
        if x_data is None:
            raise TypeError(f"X data for {self.__class__.__name__} prediction must be non-empty.")
        if self.model is None:
            raise RuntimeError(f"The {self.__class__.__name__} model is not trained yet!")

        y_pred = self.model.predict(x_data)
        return y_pred


class ReducerDataModel(BaseDataModel):
    """Contains the artifacts for dimensionality reduction."""
    def __init__(self, x_data: pd.DataFrame, x_train: pd.DataFrame, y: np.ndarray, components: int):
        super().__init__(x_data, x_train, y)
        self.components = components


class BaseReducer(BaseActionClass):
    """Parent class for all reducers (decomposition-performing classes), containing basic shared utilities."""

    def __init__(self, settings: BaseSettings, data: BaseDataModel):
        super().__init__(settings, data)
        self.array_scores: Optional[np.ndarray] = None
        self.components: Optional[int] = None
    
    @abstractmethod
    def export_data(self) -> BaseDataModel:
        pass
    
    def reduce(self, data: BaseDataModel) -> BaseDataModel:
        """Reduces dimensionality of data."""
        if self.model is None:
            raise RuntimeError(
                "The model hasn't been trained yet! You cannot use it to reduce data dimensionality."
            )
        x_data = pd.DataFrame(self.model.transform(data.x_data))
        y_dataframe = pd.DataFrame(data.y)
        x_train = pd.concat(
            [y_dataframe, x_data],
            axis=1
        )
        return BaseDataModel(
            x_data=x_data,
            x_train=x_train,
            y=data.y
        )

    @property
    @abstractmethod
    def rescaled_data(self) -> BaseDataModel:
        pass
