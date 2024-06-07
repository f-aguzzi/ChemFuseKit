'''Linear Discriminant Analysis module'''
from copy import copy
from typing import Optional

import joblib
import numpy as np
import pandas as pd

from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LD

from chemfusekit.lldf import LLDFDataModel
from chemfusekit.__utils import graph_output, run_split_test
from chemfusekit.__utils import print_confusion_matrix, print_table, GraphMode
from .__base import BaseDataModel, BaseClassifier, BaseSettings
from .pca import PCADataModel


class LDASettings(BaseSettings):
    '''Holds the settings for the LDA object.'''
    def __init__(self, components: int = 3, output: GraphMode = GraphMode.NONE, test_split: bool = False):
        super().__init__(output, test_split)
        if components <= 2:
            raise ValueError("Invalid component number: must be a > 1 integer.")
        self.components = components


class LDA(BaseClassifier):
    '''Class to store the data, methods and artifacts for Linear Discriminant Analysis'''
    def __init__(self, settings: LDASettings, data: BaseDataModel):
        super().__init__(settings, data)
        self.settings = settings
        self.data = data
        # Self-detect components if the data is from PCA
        if isinstance(data, PCADataModel):
            self.settings.components = data.components - 1

    def lda(self):
        '''Performs Linear Discriminant Analysis'''

        lda = LD(n_components=self.settings.components) # N-1 where N are the classes
        scores_lda = lda.fit(self.data.x_data, self.data.y).transform(self.data.x_data)
        pred = lda.predict(self.data.x_data)

        print_table(
            [f"LV{i+1}" for i in range(scores_lda.shape[1])],
            list(zip(*scores_lda)),
            "LDA scores",
            self.settings.output
        )

        print_table(
            ["Class", "Prior Probability"],
            [list(range(len(lda.priors_))), lda.priors_],
            "LDA Priors",
            self.settings.output
        )
        means_values = [[f"Feature {i+1}" for i in range(lda.means_.shape[1])]] + [list(lda.means_[i, :]) for i in range(lda.means_.shape[0])]
        
        print_table(
            ["Feature"] + [f"Class {i+1}" for i in range(lda.means_.shape[0])], 
            means_values,
            "LDA Class Means",
            self.settings.output
        )
        print_table(
            ["Component"] + [f"Feature {i+1}" for i in range(lda.coef_.shape[0])],
            [[f"Component {i+1}" for i in range(min(self.settings.components, lda.coef_.shape[1]))]] + [list(lda.coef_[:self.settings.components, i]) for i in range(lda.coef_.shape[0])],
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

        lv_cols = [f'LV{i+1}' for i in range(self.settings.components)]
        scores = pd.DataFrame(data=scores_lda, columns=lv_cols)     # latent variables
        scores.index = self.data.x_data.index
        y_dataframe = pd.DataFrame(self.data.y, columns=['Substance'])

        scores = pd.concat([scores, y_dataframe], axis = 1)

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
                LD(n_components=self.settings.components),
                mode=self.settings.output
            )

    def import_model(self, import_path: str):
        model_backup = copy(self.model)
        super().import_model(import_path)
        if not isinstance(self.model, LD):
            self.model = model_backup
            raise ImportError("The file you tried to import is not a LinearDiscriminantAnalysis classifier.")
        self.settings.components = self.model.n_components
