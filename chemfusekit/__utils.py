'''Utilities module: functions that are shared between different classes'''
from sklearn.cross_decomposition import PLSRegression as PLSR
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report

import numpy as np
import pandas as pd

import plotly.express as px
import plotly.graph_objects as go
import seaborn as sns
import matplotlib.pyplot as plt

from tabulate import tabulate

from enum import Enum, auto

class GraphMode(Enum):
    TEXT = auto()
    GRAPHIC = auto()
    NONE = auto()

def graph_output(scores, model, name: str, mode: GraphMode = GraphMode.GRAPHIC):
    '''A reusable graphing function.'''
    # Return early if output is disabled
    if mode is GraphMode.NONE:
        return

    # Text-mode output
    if mode is GraphMode.TEXT:
        print(f"{name} scores:\n {scores}")

        print(f"""
            explained variance ratio with {name}:
            {model.explained_variance_ratio_}
        """)

        # Display the explained variance ratio
        print("Explained Variance Ratio:", model.explained_variance_ratio_)
    
    if mode is GraphMode.GRAPHIC:
        # Scores table
        print_table(
            scores.columns,
            [scores.iloc[:, i] for i in range(scores.shape[1])],
            f"{name} Scores"
        )

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


def print_table(header_values, cell_values, title: str, mode: GraphMode = GraphMode.GRAPHIC):
    '''Multimodal table printing utility.'''
    # Return early if output is disabled
    if mode is GraphMode.NONE:
        return
    # Graphical table printing
    elif mode is GraphMode.GRAPHIC:
        fig = go.Figure(data=[go.Table(
        header=dict(values=header_values,
                    fill_color='paleturquoise',
                    align='left'),
        cells=dict(values=cell_values,
                fill_color='lavender',
                align='left'))
        ])
        fig.update_layout(title=title)
        fig.show()

    # Text-based table printing
    else:
        # Print the title
        print(f"\n\n{title}:")

        # Print the table using tabulate
        print(tabulate(np.transpose(cell_values), headers=header_values, tablefmt="rounded_outline"))


def run_split_test(x, y, model, extended=False, mode: GraphMode = GraphMode.GRAPHIC):
    '''A function to run split tests on trained models.'''

    # Return early if there's nothing to print
    if mode is GraphMode.NONE:
        return

    x_train, x_test, y_train, y_test = train_test_split(
        x,
        y,
        test_size=0.3,
        random_state=42,
        shuffle=True,
        stratify=y
    )

    model.fit(x_train, y_train)
    y_pred = model.predict(x_train)

    # TODO: add something to print _x_scores multimodally

    if extended:
        probabilities = model.predict_proba(x_train)
        score = model.score(x_train, y_train)
        predictions = model.predict(x_train)

        # See the classes the model used
        classes = model.classes_
        if isinstance(model, LogisticRegression) and len(classes == 2):     # Binary classifier
            classes = [" / ".join(classes)]
            classes = np.asarray(classes)
            classes = classes.reshape((1, 1))
        else:   # All other cases
            classes = classes.reshape((1, len(classes)))

        coefficients = model.coef_.transpose()
        intercepts = model.intercept_.reshape((1, len(model.intercept_)))
        print_table(
            ["Class"] + [f"Coefficient {i + 1}" for i in range(model.coef_.shape[1])] + ["Intercept (bias)"],
            np.concatenate((classes, coefficients, intercepts)),
            "LR Coefficients + Intercept (split test, training set)",
            mode
        )

        # Training predictions table
        sample_column = y_train.reshape((1, y_train.shape[0]))
        pred_column = predictions.reshape((1, predictions.shape[0]))
        prob_column = probabilities.transpose()

        classes = np.unique(y_train)

        print_table(
            np.concatenate((np.asarray(["True", "Prediction"]), classes)),
            np.concatenate((
                sample_column,
                pred_column,
                prob_column
            )),
            f"LR Predictions with class probabilities (split test, evaluation set, overall score: {score})",
            mode
        )

        print_confusion_matrix(
            y1=y_train,
            y2=predictions,
            title="Confusion matrix based on training set",
            mode=mode
        )

        # Test predictions set table
        probabilities = model.predict_proba(x_test)
        score = model.score(x_test, y_test)
        predictions = model.predict(x_test)
        pred_column = predictions.reshape((1, predictions.shape[0]))
        prob_column = probabilities.transpose()

        print_table(
            np.concatenate((np.asarray(["Prediction"]), classes)),
            np.concatenate((
                pred_column,
                prob_column
            )),
            f"LR Predictions with class probabilities (split test, evaluation set, overall score: {score})",
            mode
        )

    y_pred = model.predict(x_test)
    if isinstance(model, PLSR):
        y_pred = np.int8(np.abs(np.around(y_pred, decimals=0)))

    print_confusion_matrix(
        y1=y_test,
        y2=y_pred,
        title="Confusion matrix based on evaluation set",
        mode=mode
    )


def print_confusion_matrix(y1, y2, title: str, mode: GraphMode = GraphMode.GRAPHIC):
    '''Function to simplify the plotting of confusion matrices'''

    # Return early if there's nothing to print
    if mode is GraphMode.NONE:
        return

    cm = confusion_matrix(y1, y2)

    # Get unique class labels from y_true
    class_labels = sorted(set(y2))
    
    # Create the report
    report = classification_report(y1, y2, digits=2, output_dict=True)

    if mode is GraphMode.TEXT:
        print(f"\n{title}\n{cm}\n")

    elif mode is GraphMode.GRAPHIC:
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
        plt.title(title)
        plt.show()

    # Plot the classification report
    cr = pd.DataFrame(report).transpose()

    # Create a Plotly table
    print_table(
        ['substance'] + list(cr.columns),
        [cr.index, cr['precision'], cr['recall'], cr['f1-score'], cr['support']],
        "Classification Report",
        mode 
    )
