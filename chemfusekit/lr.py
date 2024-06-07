'''Logistic Regression Module'''
from copy import copy
from typing import Optional

import numpy as np
import pandas as pd

from sklearn.linear_model import LogisticRegression

from chemfusekit.__utils import run_split_test, print_confusion_matrix, print_table, GraphMode
from .__base import BaseSettings, BaseDataModel, BaseClassifier
from .pca import PCADataModel


class LRSettings(BaseSettings):
    '''Holds the settings for the LR object.'''
    def __init__(self, algorithm: str = 'liblinear', output: GraphMode = GraphMode.NONE, test_split: bool = False):
        super().__init__(output, test_split)
        if algorithm not in [
            'lbfgs',
            'liblinear',
            'newton-cg',
            'newton-cholesky',
            'sag',
            'saga'
        ]:
            raise ValueError(f"{algorithm}: this algorithm does not exist.")
        self.algorithm = algorithm


class LR(BaseClassifier):
    '''Class to store the data, methods and artifacts for Logistic Regression'''
    def __init__(self, settings: LRSettings, data: BaseDataModel):
        super().__init__(settings, data)
        if isinstance(data, PCADataModel):
            self.array_scores = data.array_scores
        else:
            self.array_scores = data.x_train.drop('Substance', axis=1).values

    def lr(self):
        '''Performs Logistic Regression'''

        # Let's build our model on the training set
        model = LogisticRegression(
            solver=self.settings.algorithm,
            random_state=0,
            class_weight='balanced',
            max_iter=10000
        ).fit(self.array_scores, self.data.y)

        # See the classes the model used
        classes = np.unique(self.data.y)
        classes = classes.reshape((1, len(classes)))
        coefficients = model.coef_.transpose()
        intercepts = model.intercept_.reshape((1, len(model.intercept_)))
        print_table(
            ["Class"] + [f"Coefficient {i+1}" for i in range(model.coef_.shape[1])] + ["Intercept (bias)"],
            np.concatenate((classes, coefficients, intercepts)),
            "LR Coefficients",
            self.settings.output
        )

        '''
        Evaluate the model: each sample has a probability of belonging to Positive
        or Negative outcome. Class 0 is Negative, class 1 is Positive.  If the value
        of the first column (probability of being Negative) is higher than 0.5, we
        have a Negative sample. Otherwise, it will be Positive
        '''

        probabilities = model.predict_proba(self.array_scores)
        predictions = model.predict(self.array_scores)

        # This tells us the accuracy of our model in calibration
        scores = model.score(self.array_scores, self.data.y)

        # Save the trained model
        self.model = model

        sample_column = self.data.y.reshape((1, self.data.y.shape[0]))
        pred_column = predictions.reshape((1, predictions.shape[0]))
        prob_column = probabilities.transpose()

        print_table(
            np.concatenate((np.asarray(["Real sample", "Prediction"]), classes.reshape(17, ))),
            np.concatenate((
                sample_column,
                pred_column,
                prob_column
            )),
            f"LR Predictions with class probabilities (overall score: {scores}",
            self.settings.output
        )

        print_confusion_matrix(
            self.data.y,
            predictions,
            "Confusion Matrix based on whole data set",
            self.settings.output
        )

        if self.settings.test_split:
            split_model = LogisticRegression(
                solver=self.settings.algorithm,
                random_state=0,
                class_weight='balanced',
                max_iter=10000
            )

            run_split_test(
                self.array_scores,
                self.data.y,
                split_model,
                extended=True,
                mode=self.settings.output
            )

    def predict(self, x_sample: pd.DataFrame):
        '''Performs LR prediction once the model is trained.'''
        prediction = super().predict(x_sample)
        probabilities = self.model.predict_proba(x_sample)

        classes = self.model.classes_.reshape((self.model.classes_.shape[0], ))
        probabilities = probabilities.reshape((self.model.classes_.shape[0], ))
        print_table(
            classes,
            probabilities,
            f"Predicted class: {prediction}. Scores:",
            mode=self.settings.output
        )

        return prediction

    def import_model(self, import_path: str):
        model_backup = copy(self.model)
        super().import_model(import_path)
        if not isinstance(self.model, LogisticRegression):
            self.model = model_backup
            raise ImportError("The file you tried to import is not a LogisticRegression classifier.")
        self.settings.algorithm = self.model.solver
