'''Linear Discriminant Analysis module'''
import numpy as np
import pandas as pd

from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LD
from sklearn.model_selection import train_test_split

from sklearn.metrics import confusion_matrix, classification_report

import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

class LDASettings:
    '''Holds the settings for the LDA object.'''
    def __init__(self, components=3, output=False):
        if components <= 2:
            raise ValueError("Invalid component number: must be a > 1 integer.")
        self.components = components
        self.output = output

class LDA:
    '''Class to store the data, methods and artifacts for Linear Discriminant Analysis'''
    def __init__(self, lldf_model, settings):
        if lldf_model is None:
            raise TypeError("The LLDF model for LDA cannot be null.")
        if settings is None:
            raise TypeError("The LDA settings object cannot be null.")
        self.settings = settings
        self.x_data = lldf_model.x_data
        self.x_train = lldf_model.x_train
        self.y = lldf_model.y
        self.model = None

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

        if self.settings.output:
            print(scores)

            print(f"""
                explained variance ratio (three components) with LDA:
                {lda.explained_variance_ratio_}
            """)

            # Display the explained variance ratio
            print("Explained Variance Ratio:", lda.explained_variance_ratio_)

            #Scores plot
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
                                hover_name=scores.index
            )
            fig.update_layout(
            title_text='3D colored by Substance for Linear Discriminant Analysis')
            fig.show()

        lda2 = LD(n_components=self.settings.components)

        self.x_train, x_test, y_train, y_test = train_test_split(
            (scores.drop('Substance', axis=1).values),
            self.y,
            test_size=0.3,
            random_state=42
        )

        lda2.fit(self.x_train, y_train)
        lda2.predict(x_test)
        y_pred = lda2.predict(x_test)

        if self.settings.output:
            self.__print_prediction_graphs(y_test, y_pred)

        self.model = lda

    def __print_prediction_graphs(self, y_test, y_pred):
        '''Helper function to print graphs and stats about LDA predictions.'''
        # Assuming 'y_test' and 'y_pred' are your true and predicted labels
        cm = confusion_matrix(y_test, y_pred)

        # Get unique class labels from y_true
        class_labels = sorted(set(y_test))

        # Plot the confusion matrix using seaborn with custom colormap (Blues)
        sns.heatmap(cm,
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
        print(classification_report(y_test, y_pred, digits=2))

    def predict(self, x_data):
        '''Performs LDA prediction once the model is trained.'''
        if x_data is None:
            raise TypeError("X data for LDA prediction must be non-empty.")
        if self.model is None:
            raise RuntimeError("The LDA model is not trained yet!")

        y_pred = self.model.predict(x_data)
        return y_pred
