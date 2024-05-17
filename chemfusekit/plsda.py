'''Partial Least Squares Discriminant Analysis module.'''
import pandas as pd
import numpy as np

import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt

from sklearn.preprocessing import scale
from sklearn.cross_decomposition import PLSRegression as PLSR
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report


from chemfusekit.lldf import LLDFModel

class PLSDASettings:
    '''Holds the settings for the PLSDA object.'''
    def __init__(self, n_components=3, output=False, test_split=False):
        if n_components < 1:
            raise ValueError("Invalid n_components number: should be a positive integer.")
        if type(output) is not bool:
            print(type(output))
            raise TypeError("Invalid output: should be a boolean value.")
        if type(test_split) is not bool:
            raise TypeError("Invalid test_split: should be a boolean value.")
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
        if type(settings) is not PLSDASettings:
            raise TypeError("Invalid settings: should be a PLSDASettings-class object")
        if type(fused_data) is not LLDFModel:
            raise TypeError("Invalid fused_data: should be a LLDFModel-class object")
        self.settings = settings
        self.fused_data = fused_data
        self.model: PLSR = None

    def plsda(self):
        '''Performs Partial Least Squares Discriminant Analysis'''
        x = scale(self.fused_data.x_data.values)
        y = self.fused_data.x_train.Substance.astype('category').cat.codes

        regr_pls = PLSR(self.settings.n_components)
        regr_pls.fit_transform(x,y)

        # Save the model
        self.model = regr_pls

        if self.settings.output:
            regr_pls.fit_transform(x,y)
            print(regr_pls.x_scores_)

            # Scores
            scores = regr_pls.x_scores_
            scores = pd.DataFrame(scores, columns = ['LV1','LV2','LV3'])
            scores.index = self.fused_data.x_train.index
            y = self.fused_data.x_train.Substance
            scores = pd.concat([scores, y], axis = 1)
            print(scores)

            # Loadings
            loadings = pd.DataFrame(regr_pls.x_loadings_,columns = ["LV1",'LV2','LV3'])
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
            pred=regr_pls.predict(self.fused_data.x_data)
            print(pred)

            pred = np.abs(np.around(pred, decimals= 0))
            print(pred)

            # Confusion matrix
            # Assuming 'y_true' and 'y_pred' are your true and predicted labels
            cm = confusion_matrix(y, pred)

            # Get unique class labels from y_true
            class_labels = sorted(set(y))

            # Plot the confusion matrix using seaborn with custom colormap (Blues)
            sns.heatmap(
                cm,
                annot=True,
                fmt='d',
                cmap='Blues',
                xticklabels=class_labels,
                yticklabels=class_labels,
                cbar=False,
                vmin=0,
                vmax=cm.max()
            )

            plt.xlabel('Predicted')
            plt.ylabel('True')
            plt.title('Confusion Matrix based on training set')
            plt.show()

            # Print the classification report
            print(classification_report(y, pred, digits=2))

        if self.settings.output and self.settings.test_split:
            x_train, x_test, y_train, y_test = train_test_split(
                self.fused_data.x_data,
                y,
                train_size=0.7,
                shuffle=True,
                stratify=y)

            regr_pls = PLSR(self.settings.n_components)
            regr_pls.fit_transform(x_train,y_train)
            print(regr_pls.x_scores_)

            pred = regr_pls.predict(x_test)
            print(pred)

            pred= np.abs(np.around(pred, decimals= 0))
            print(pred)

            # Assuming 'y_true' and 'y_pred' are your true and predicted labels
            # Assuming 'y_true' and 'y_pred' are your true and predicted labels
            cm = confusion_matrix(y_test, pred)

            # Get unique class labels from y_true
            class_labels = sorted(set(y_test))

            # Plot the confusion matrix using seaborn with custom colormap (Blues)
            sns.heatmap(
                cm,
                annot=True,
                fmt='d',
                cmap='Blues',
                xticklabels=class_labels,
                yticklabels=class_labels,
                cbar=False,
                vmin=0,
                vmax=cm.max()
            )

            plt.xlabel('Predicted')
            plt.ylabel('True')
            plt.title('Confusion Matrix based on evaluation set')
            plt.show()

            # Print the classification report
            print(classification_report(y_test, pred, digits=2))

    def predict(self, x_data):
        '''Performs PLSDA prediction once the model is trained.'''
        if x_data is None:
            raise TypeError("X data for PLSDA prediction must be non-empty.")
        if self.model is None:
            raise RuntimeError("The PLSDA model is not trained yet!")

        y_pred = self.model.predict(x_data)
        return y_pred
