'''Linear Discriminant Analysis module'''
from typing import Optional

import numpy as np
import pandas as pd

from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LD

from chemfusekit.lldf import LLDFModel
from chemfusekit.__utils import graph_output, run_split_test
from chemfusekit.__utils import print_confusion_matrix, print_table, GraphMode

class LDASettings:
    '''Holds the settings for the LDA object.'''
    def __init__(self, components: int = 3, output: GraphMode = GraphMode.NONE,
                 test_split: bool = False):
        if components <= 2:
            raise ValueError("Invalid component number: must be a > 1 integer.")
        if test_split is True and output is GraphMode.NONE:
            raise Warning(
                "You selected test_split but it won't run because you disabled the output."
            )
        self.components = components
        self.output = output
        self.test_split = test_split

class LDA:
    '''Class to store the data, methods and artifacts for Linear Discriminant Analysis'''
    def __init__(self, lldf_model: LLDFModel, settings: LDASettings):
        self.settings = settings
        self.x_data = lldf_model.x_data
        self.x_train = lldf_model.x_train
        self.y = lldf_model.y
        self.model: Optional[LD] = None

    def lda(self):
        '''Performs Linear Discriminant Analysis'''

        lda = LD(n_components=self.settings.components) # N-1 where N are the classes
        scores_lda = lda.fit(self.x_data, self.y).transform(self.x_data)
        pred = lda.predict(self.x_data)

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

        pred = lda.predict(self.x_data)
        print_confusion_matrix(
            y1=self.y,
            y2=pred,
            title="LDA Training Confusion Matrix",
            mode=self.settings.output
        )

        lv_cols = [f'LV{i+1}' for i in range(self.settings.components)]
        scores = pd.DataFrame(data = scores_lda, columns = lv_cols) # latent variables
        scores.index = self.x_data.index
        y_dataframe = pd.DataFrame(self.y, columns=['Substance'])

        scores = pd.concat([scores, y_dataframe], axis = 1)

        # Store the traiend model
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
                (scores.drop('Substance', axis=1).values),
                self.y,
                LD(n_components=self.settings.components),
                mode=self.settings.output
            )

    def predict(self, x_data: pd.DataFrame):
        '''Performs LDA prediction once the model is trained.'''
        if x_data is None:
            raise TypeError("X data for LDA prediction must be non-empty.")
        if self.model is None:
            raise RuntimeError("The LDA model is not trained yet!")

        y_pred = self.model.predict(x_data)
        return y_pred
