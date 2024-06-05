'''Partial Least Squares Discriminant Analysis module.'''
from copy import copy
from typing import Optional

import pandas as pd
import numpy as np

import plotly.express as px

from sklearn.cross_decomposition import PLSRegression as PLSR

from chemfusekit.lldf import LLDFDataModel
from chemfusekit.__utils import GraphMode, print_table, print_confusion_matrix, run_split_test
from .__base import BaseSettings, BaseDataModel, BaseClassifier


class PLSDASettings(BaseSettings):
    '''Holds the settings for the PLSDA object.'''
    def __init__(self, n_components: int = 3, output: GraphMode = GraphMode.NONE, test_split: bool = False):
        super().__init__(output, test_split)
        if n_components < 1:
            raise ValueError("Invalid n_components number: should be a positive integer.")
        self.n_components = n_components


class PLSDA(BaseClassifier):
    '''
    Class to store the data, methods and artifacts for Partial Least Squares
    Discriminant Analysis
    '''
    def __init__(self, settings: PLSDASettings, data: BaseDataModel):
        super().__init__(settings, data)

    def plsda(self):
        '''Performs Partial Least Squares Discriminant Analysis'''
        x = self.data.x_data
        y = self.data.x_train.Substance.astype('category').cat.codes

        regr_pls = PLSR(n_components=self.settings.n_components)
        regr_pls.fit_transform(x, y)

        # Save the model
        self.model = copy(regr_pls)

        # Re-create the model
        regr_pls_2 = PLSR(n_components=self.settings.n_components)
        regr_pls_2.fit_transform(x, y)

        # Scores and loadings
        lv_cols = [f"LV{i + 1}" for i in range(self.settings.n_components)]
        scores = pd.DataFrame(regr_pls_2.x_scores_, columns=lv_cols)
        scores.index = self.data.x_train.index
        y = self.data.x_train.Substance
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

        if self.settings.output is GraphMode.GRAPHIC:
            # Scores plot
            fig = px.scatter(scores, x="LV1", y="LV2", color="Substance", hover_data=['Substance'])
            fig.update_xaxes(zeroline=True, zerolinewidth=1, zerolinecolor='Black')
            fig.update_yaxes(zeroline=True, zerolinewidth=1, zerolinecolor='Black')
            fig.update_layout(
                height=600,
                width=800,
                title_text='Scores Plot')
            fig.show()

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
            fig = px.scatter(loadings, x="LV1", y="LV2",text="Attributes")
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
            pred = np.int8(np.round(pred, decimals=0))
            classes = np.unique(y)
            for i in range(len(np.unique(pred)) - len(classes)):
                classes = np.append(classes, f'Unknown substance {i}')
            predicted_substances = [classes[p-3] for p in pred]
            print_table(
                ["Sample number", "True", "Predicted"],
                np.stack((
                    [f"{i+1}" for i in range(len(pred))],
                    y,
                    predicted_substances
                )),
                "True and predicted substances",
                self.settings.output
            )

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
            run_split_test(x, y, PLSR(self.settings.n_components), mode=self.settings.output)

    def import_model(self, import_path: str):
        model_backup = copy(self.model)
        super().import_model(import_path)
        if not isinstance(self.model, PLSR):
            self.model = model_backup
            raise ImportError("The file you tried to import is not a PLSRegression classifier.")
        self.settings.n_components = self.model.n_components
