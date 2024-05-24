'''Logistic Regression Module'''
from typing import Optional

import numpy as np
import pandas as pd

from sklearn.linear_model import LogisticRegression

from chemfusekit.__utils import run_split_test, print_confusion_matrix, print_table, GraphMode

class LRSettings:
    '''Holds the settings for the LR object.'''
    def __init__(self, algorithm: str = 'liblinear', output: GraphMode = GraphMode.NONE,
                 test_split: bool = False):
        if algorithm not in [
            'lbfgs',
            'liblinear',
            'newton-cg',
            'newton-cholesky',
            'sag',
            'saga'
        ]:
            raise ValueError(f"{algorithm}: this algorithm does not exist.")
        if test_split is True and output is GraphMode.NONE:
            raise Warning(
                "You selected test_split but it won't run because you disabled the output."
            )
        self.algorithm = algorithm
        self.output = output
        self.test_split = test_split


class LR:
    '''Class to store the data, methods and artifacts for Logistic Regression'''
    def __init__(self, settings: LRSettings, array_scores: np.ndarray, y: np.ndarray):
        self.settings = settings
        self.array_scores = array_scores
        self.y = y
        self.model: Optional[LogisticRegression] = None

    def lr(self):
        '''Performs Logistic Regression'''

        # Let's build our model on the training set
        model = LogisticRegression(
            solver=self.settings.algorithm,
            random_state=0,
            class_weight='balanced',
            max_iter=10000
        ).fit(self.array_scores, self.y)

        # See the classes the model used
        classes = np.unique(self.y)
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
        scores = model.score(self.array_scores, self.y)

        # Save the trained model
        self.model = model

        sample_column = self.y.reshape((1, self.y.shape[0]))
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
            self.y,
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
                self.y,
                split_model,
                extended=True,
                mode=self.settings.output
            )

    def predict(self, x_sample: pd.DataFrame):
        '''Performs LR prediction once the model is trained.'''
        if self.model is None:
            raise RuntimeError("The LR model is not trained yet!")

        prediction = self.model.predict(x_sample)
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
