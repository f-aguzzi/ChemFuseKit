'''Linear Discriminant Analysis module'''
from typing import Optional

import numpy as np
import pandas as pd

from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LD
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report

import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

from chemfusekit.lldf import LLDFModel
from chemfusekit.__utils import graph_output, run_split_test

class LDASettings:
    '''Holds the settings for the LDA object.'''
    def __init__(self, components: int = 3, output: bool = False, test_split: bool = False):
        if components <= 2:
            raise ValueError("Invalid component number: must be a > 1 integer.")
        if test_split is True and output is False:
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

        if self.settings.output:
            print(f"LDA scores:\n{scores_lda}")
            print(lda.priors_)
            print(lda.means_)
            print(lda.coef_[0:self.settings.components,:])
            pred=lda.predict(self.x_data)
            print(np.unique(pred, return_counts=True))

            print(confusion_matrix(pred, self.y))
            print(classification_report(self.y, pred, digits=2))

        lv_cols = [f'LV{i+1}' for i in range(self.settings.components)]
        scores = pd.DataFrame(data = scores_lda, columns = lv_cols) # latent variables
        scores.index = self.x_data.index
        y_dataframe = pd.DataFrame(self.y, columns=['Substance'])

        scores = pd.concat([scores, y_dataframe], axis = 1)

        # Store the traiend model
        self.model = lda

        # Show graphs if required by the user
        if self.settings.output:
            graph_output(scores, self.model, "Linear Discriminant Analysis")
            
            # Run split tests if required by the user
            if self.settings.test_split:
                run_split_test(
                    (scores.drop('Substance', axis=1).values),
                    self.y,
                    LD(n_components=self.settings.components)
                )

    def predict(self, x_data: pd.DataFrame):
        '''Performs LDA prediction once the model is trained.'''
        if x_data is None:
            raise TypeError("X data for LDA prediction must be non-empty.")
        if self.model is None:
            raise RuntimeError("The LDA model is not trained yet!")

        y_pred = self.model.predict(x_data)
        return y_pred
