'''Utilities model: functions that are shared between different classes'''
from sklearn.cross_decomposition import PLSRegression as PLSR
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report

import numpy as np

import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

def graph_output(scores, model, name: str):
    '''A reusable graphing function.'''
    print(scores)
    print(f"""
        explained variance ratio with {name}:
        {model.explained_variance_ratio_}
    """)

    # Display the explained variance ratio
    print("Explained Variance Ratio:", model.explained_variance_ratio_)

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
    fig.update_layout(title_text=f"3D colored by Substance for {name}")
    fig.show()

def run_split_test(x, y, model, extended=False):
    '''A function to run split tests on trained models.'''
    x_train, x_test, y_train, y_test = train_test_split(
        x,
        y,
        test_size=0.3,
        random_state=42,
        shuffle=True,
        stratify=y
    )

    model.fit(x_train, y_train)
    y_pred = model.predict(x_test)

    # TODO: add something to print _x_scores multimodally

    if extended:
        # We can see the classes the model used
        print(model.classes_)
        # See the intercept of the model
        print(model.intercept_)
        # See the coefficients of the model - that can be easily interpreted
        # (correlating or not with y)
        print(model.coef_)

        '''
        Evaluate the model: each sample has a probability of belonging to Positive
        or Negative outcome. Class 0 is Negative, class 1 is Positive.  If the value
        of the first column (probability of being Negative) is higher than 0.5, we
        have a Negative sample. Otherwise, it will be Positive
        '''
        probabilities = model.predict_proba(x_train)
        print(probabilities)

        # This tells us the accuracy of our model in calibration
        model.score(x_train, y_train)

        predictions = model.predict(x_train)

        print("Calibration predictions: ")
        print(predictions)
        print_confusion_matrix(y_train, predictions, "Confusion matrix based on training set")
 
    if isinstance(model, PLSR):
        y_pred = np.int8(np.abs(np.around(y_pred, decimals=0)))

    print_confusion_matrix(y_test, y_pred, "Confusion matrix based on evaluation set")

# TODO: make multimodal
def print_confusion_matrix(y1, y2, title):
    '''Function to simplify the plotting of confusion matrices'''
    cm = confusion_matrix(y1, y2)

    # Get unique class labels from y_true
    class_labels = sorted(set(y2))

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
    plt.title(title)
    plt.show()

    # Print the classification report
    print(classification_report(y1, y2, digits=2))
