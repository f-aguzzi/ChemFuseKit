'''Partial Least Squares Discriminant Analysis module.'''
from typing import Optional

import pandas as pd
import numpy as np

import plotly.express as px

from sklearn.cross_decomposition import PLSRegression as PLSR

from chemfusekit.lldf import LLDFModel
from chemfusekit.__utils import print_confusion_matrix, run_split_test


class PLSDASettings:
    '''Holds the settings for the PLSDA object.'''
    def __init__(self, n_components: int = 3, output: bool = False, test_split: bool = False):
        if n_components < 1:
            raise ValueError("Invalid n_components number: should be a positive integer.")
        if test_split is True and output is False:
            raise Warning(
                "You selected test_split but it won't run because you disabled the output."
            )
        self.n_components = n_components
        self.output = output
        self.test_split = test_split

class PLSDA:
    '''
    Class to store the data, methods and artifacts for Partial Least Squares
    Discriminant Analysis
    '''
    def __init__(self, settings: PLSDASettings, fused_data: LLDFModel):
        self.settings = settings
        self.fused_data = fused_data
        self.model: Optional[PLSR] = None

    def plsda(self):
        '''Performs Partial Least Squares Discriminant Analysis'''
        x = self.fused_data.x_data
        y = self.fused_data.x_train.Substance.astype('category').cat.codes

        regr_pls = PLSR(n_components=self.settings.n_components)
        regr_pls.fit_transform(x,y)

        # Save the model
        self.model = regr_pls

        if self.settings.output:
            # Re-create the model
            regr_pls_2 = PLSR(n_components=self.settings.n_components)
            regr_pls_2.fit_transform(x,y)

            # Scores
            scores = regr_pls_2.x_scores_
            lv_cols = [f"LV{i+1}" for i in range(self.settings.n_components)]
            scores = pd.DataFrame(scores, columns = lv_cols)
            scores.index = self.fused_data.x_train.index
            y = self.fused_data.x_train.Substance
            scores = pd.concat([scores, y], axis = 1)
            print(scores)

            # Loadings
            loadings = pd.DataFrame(regr_pls.x_loadings_,columns = lv_cols)
            loadings["Attributes"] = self.fused_data.x_train.iloc[:,1:].columns
            print(loadings)

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
            pred = np.int8(np.abs(np.around(pred, decimals=0)))
            print(f"Predicted data:\n\n{pred}")

            # Print confusion matrix
            y = self.fused_data.x_train.Substance.astype('category').cat.codes 
            print_confusion_matrix(y, pred, "Confusion Matrix based on training set")


        if self.settings.output and self.settings.test_split:
            x = self.fused_data.x_data
            y = self.fused_data.x_train.Substance.astype('category').cat.codes
            run_split_test(x, y, PLSR(self.settings.n_components))

    def predict(self, x_data: pd.DataFrame):
        '''Performs PLSDA prediction once the model is trained.'''
        if x_data is None:
            raise TypeError("X data for PLSDA prediction must be non-empty.")
        if self.model is None:
            raise RuntimeError("The PLSDA model is not trained yet!")

        y_pred = self.model.predict(x_data)
        return y_pred
