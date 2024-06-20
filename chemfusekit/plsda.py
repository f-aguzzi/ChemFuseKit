"""Partial Least Squares Discriminant Analysis module."""
from copy import copy
from functools import cached_property

import numpy as np
import pandas as pd
import plotly.express as px
from sklearn.cross_decomposition import PLSRegression as PLSR
from sklearn.model_selection import cross_val_score

from chemfusekit.__utils import print_table, print_confusion_matrix, run_split_test, GraphMode
from .__base import BaseClassifierSettings, BaseDataModel, BaseClassifier, BaseReducer, ReducerDataModel


class PLSDASettings(BaseClassifierSettings):
    """Holds the settings for the PLSDA object."""

    def __init__(self, components: int | None = None, output: str = 'none', test_split: bool = False):
        super().__init__(output, test_split)
        if components is not None and components < 1:
            raise ValueError("Invalid n_components number: should be a positive integer.")
        self.components = components


class PLSDA(BaseClassifier, BaseReducer):
    """
    Class to store the data, methods and artifacts for Partial Least Squares
    Discriminant Analysis
    """

    def export_data(self) -> ReducerDataModel:
        """Exports the artifacts of PLSDA dimensionality reduction."""
        return ReducerDataModel(
            x_data=self.data.x_data,
            x_train=self.data.x_train,
            y=self.data.y,
            components=self.components
        )

    @cached_property
    def rescaled_data(self) -> BaseDataModel:
        """A read-only property that returns the rescaled data."""
        data_model = self.reduce(self.data)
        return data_model

    def __init__(self, settings: PLSDASettings, data: BaseDataModel):
        super().__init__(settings, data)
        self.components = settings.components

    def train(self):
        """Performs Partial Least Squares Discriminant Analysis"""
        x = self.data.x_data
        y = self.data.x_train.Substance.astype('category').cat.codes

        # Auto-select the number of components only if the current number is null
        if self.components is None:
            self._select_feature_number(x, y)

        # Re-create the model
        regr_pls = PLSR(n_components=self.components)
        regr_pls.fit(x, y)

        # Save the model
        self.model = copy(regr_pls)

        # Scores and loadings
        lv_cols = [f"LV{i + 1}" for i in range(self.components)]
        scores = pd.DataFrame(regr_pls.x_scores_, columns=lv_cols)
        scores.index = self.data.x_train.index
        y = pd.DataFrame(self.data.y, columns=['Substance'])
        scores = pd.concat([scores, y], axis=1)

        print_table(
            scores.columns,
            scores.transpose(),
            "PLSDA scores by substance",
            self.settings.output
        )

        # Loadings
        loadings = pd.DataFrame(regr_pls.x_loadings_, columns=lv_cols)
        loadings["Attributes"] = self.data.x_train.iloc[:, 1:].columns
        print_table(
            loadings.columns,
            loadings.transpose(),
            "PLSDA Loadings",
            self.settings.output
        )

        if self.settings.output is GraphMode.GRAPHIC and self.components >= 2:
            # Scores plot
            fig = px.scatter(scores, x="LV1", y="LV2", color="Substance", hover_data=['Substance'])
            fig.update_xaxes(zeroline=True, zerolinewidth=1, zerolinecolor='Black')
            fig.update_yaxes(zeroline=True, zerolinewidth=1, zerolinecolor='Black')
            fig.update_layout(
                height=600,
                width=800,
                title_text='Scores Plot')
            fig.show()

            if self.components >= 3:
                # Plot 3D scores
                fig = px.scatter_3d(scores, x='LV1', y='LV2', z='LV3',
                                    color='Substance', hover_data=['Substance'],
                                    hover_name=scores.index)
                fig.update_xaxes(zeroline=True, zerolinewidth=1, zerolinecolor='Black')
                fig.update_yaxes(zeroline=True, zerolinewidth=1, zerolinecolor='Black')
                fig.update_layout(
                    title_text='Scores 3D Plot colored by Class using the raw data')
                fig.show()

            # Loadings plot
            fig = px.scatter(loadings, x="LV1", y="LV2", text="Attributes")
            fig.update_xaxes(zeroline=True, zerolinewidth=1, zerolinecolor='Black')
            fig.update_yaxes(zeroline=True, zerolinewidth=1, zerolinecolor='Black')
            fig.update_traces(textposition='top center')
            fig.update_layout(
                height=600,
                width=800,
                title_text='Loadings Plot')
            fig.show()

            # Predictions
            pred = regr_pls.predict(x)
            pred = np.int8(np.abs((np.round(pred, decimals=0) - 3)))

            # Print confusion matrix
            y = self.data.x_train.Substance.astype('category').cat.codes
            print_confusion_matrix(
                y,
                pred,
                "Confusion Matrix based on training set",
                self.settings.output
            )

        if self.settings.output and self.settings.test_split:
            x = self.data.x_data
            y = self.data.x_train.Substance.astype('category').cat.codes
            run_split_test(x, y, PLSR(self.components), mode=self.settings.output)

    def _select_feature_number(self, x, y):
        # Auto-select the number of components
        max_comps = min(self.data.x_data.shape[1], 20)
        n_components = np.arange(1, max_comps + 1)
        cv_scores = []
        for n in n_components:
            plsda = PLSR(n_components=n)
            scores = cross_val_score(plsda, x, y, cv=5)
            cv_scores.append(scores.mean())
        # Select the number of components that maximizes the cross-validated score
        self.components = n_components[np.argmax(cv_scores)]

    def import_model(self, import_path: str):
        model_backup = copy(self.model)
        super().import_model(import_path)
        if not isinstance(self.model, PLSR):
            self.model = model_backup
            raise ImportError("The file you tried to import is not a PLSRegression classifier.")
        self.settings.components = self.model.n_components
