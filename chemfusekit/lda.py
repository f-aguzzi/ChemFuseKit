"""Linear Discriminant Analysis module"""
from copy import copy
from functools import cached_property
from typing import Optional

import numpy as np
import pandas as pd

from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LD
from sklearn.model_selection import cross_val_score

from chemfusekit.__utils import graph_output, run_split_test, GraphMode
from chemfusekit.__utils import print_confusion_matrix, print_table
from .__base import BaseDataModel, BaseClassifier, BaseClassifierSettings, BaseReducer, ReducerDataModel


class LDADataModel(BaseDataModel):
    """Holds the output data from LDA."""

    def __init__(self, x_data: pd.DataFrame, x_train: pd.DataFrame, y: np.ndarray, components: int):
        super().__init__(x_data, x_train, y)
        self.components = components


class LDASettings(BaseClassifierSettings):
    """Holds the settings for the LDA object."""

    def __init__(self, components: int | None = None, output: str = 'none', test_split: bool = False):
        super().__init__(output, test_split)
        if components is not None and components <= 2:
            raise ValueError("Invalid component number: must be a > 1 integer.")
        self.components = components


class LDA(BaseClassifier, BaseReducer):
    """Class to store the data, methods and artifacts for Linear Discriminant Analysis"""

    def __init__(self, settings: LDASettings, data: BaseDataModel):
        super().__init__(settings, data)
        self.settings = settings
        self.data = data
        # Self-detect components if the data is from PCA
        if isinstance(data, ReducerDataModel):
            self.components = data.components - 1
        self.array_scores: Optional[np.ndarray] = None

    def train(self):
        """Performs Linear Discriminant Analysis"""

        # Auto-selection of the number of components if not specified
        if self.settings.components is None and self.components is None:
            self._select_feature_number(self.data.x_data, self.data.y)

        lda = LD(n_components=self.components)
        self.array_scores = lda.fit_transform(self.data.x_data, self.data.y)
        pred = lda.predict(self.data.x_data)

        print_table(
            [f"LV{i + 1}" for i in range(self.array_scores.shape[1])],
            list(zip(*self.array_scores)),
            "LDA scores",
            self.settings.output
        )

        print_table(
            ["Class", "Prior Probability"],
            [list(range(len(lda.priors_))), lda.priors_],
            "LDA Priors",
            self.settings.output
        )
        means_values = [[f"Feature {i + 1}" for i in range(lda.means_.shape[1])]] + [list(lda.means_[i, :]) for i in
                                                                                     range(lda.means_.shape[0])]

        print_table(
            ["Feature"] + [f"Class {i + 1}" for i in range(lda.means_.shape[0])],
            means_values,
            "LDA Class Means",
            self.settings.output
        )
        print_table(
            ["Component"] + [f"Feature {i + 1}" for i in range(lda.coef_.shape[0])],
            [[f"Component {i + 1}" for i in range(min(self.components, lda.coef_.shape[1]))]] + [
                list(lda.coef_[:self.components, i]) for i in range(lda.coef_.shape[1])],
            "LDA Coefficients",
            self.settings.output
        )
        classes, count = np.unique(pred, return_counts=True)
        print_table(
            ["Class", "Count"],
            [classes, count],
            "Prediction Counts",
            self.settings.output
        )

        pred = lda.predict(self.data.x_data)
        print_confusion_matrix(
            y1=self.data.y,
            y2=pred,
            title="LDA Training Confusion Matrix",
            mode=self.settings.output
        )

        lv_cols = [f'LV{i + 1}' for i in range(self.components)]
        scores = pd.DataFrame(data=self.array_scores, columns=lv_cols)  # latent variables
        scores.index = self.data.x_data.index
        y_dataframe = pd.DataFrame(self.data.y, columns=['Substance'])

        scores = pd.concat([scores, y_dataframe], axis=1)

        # Store the trained model
        self.model = lda

        # Show graphs if required by the user
        graph_output(
            scores,
            self.model,
            "Linear Discriminant Analysis",
            mode=self.settings.output
        )

        # Run split tests if required by the user
        if self.settings.test_split:
            run_split_test(
                scores.drop('Substance', axis=1).values,
                self.data.y,
                LD(n_components=self.components),
                mode=self.settings.output
            )

    def import_model(self, import_path: str):
        model_backup = copy(self.model)
        super().import_model(import_path)
        if not isinstance(self.model, LD):
            self.model = model_backup
            raise ImportError("The file you tried to import is not a LinearDiscriminantAnalysis classifier.")
        self.settings.components = self.model.n_components
        self.components = self.model.n_components

    def export_data(self) -> LDADataModel:
        """Export the data to an object."""
        return LDADataModel(
            x_data=self.data.x_data,
            x_train=self.data.x_train,
            y=self.data.y,
            components=self.components
        )

    @cached_property
    def rescaled_data(self) -> BaseDataModel:
        if self.model is None:
            settings_backup = copy(self.settings)
            self.settings.output = GraphMode.NONE
            self.settings.test_split = False
            self.train()
            self.settings = settings_backup

        x_data = pd.DataFrame(self.model.transform(self.data.x_data))
        y_dataframe = pd.DataFrame(self.data.y, columns=['Substance'])
        x_train = pd.concat(
            [y_dataframe, x_data],
            axis=1
        )

        return BaseDataModel(
            x_data,
            x_train,
            self.data.y
        )

    def _select_feature_number(self, x, y):
        # Auto-select the number of components
        max_comps = min(self.data.x_data.shape[1], 20, len(np.unique(y)))
        n_components = np.arange(1, max_comps)
        print(n_components)
        cv_scores = []
        for n in n_components:
            lda = LD(n_components=n)
            scores = cross_val_score(lda, x, y, cv=5)
            cv_scores.append(scores.mean())
        # Select the number of components that maximizes the cross-validated score
        self.components = n_components[np.argmax(cv_scores)]
