'''Logistic Regression Module'''
from typing import Optional

import numpy as np
import pandas as pd

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.model_selection import train_test_split
import seaborn as sns
import matplotlib.pyplot as plt

from chemfusekit.__utils import run_split_test, print_confusion_matrix

class LRSettings:
    '''Holds the settings for the LR object.'''
    def __init__(self, algorithm: str = 'liblinear', output: bool = False,
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
        if test_split is True and output is False:
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

        if self.settings.output:
            #we can see the classes the model used
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

        probabilities = model.predict_proba(self.array_scores)
        predictions = model.predict(self.array_scores)

        # This tells us the accuracy of our model in calibration
        scores = model.score(self.array_scores, self.y)

        # Save the trained model
        self.model = model

        if self.settings.output:
            print(probabilities)
            print(predictions)
            print(scores)

            cm = confusion_matrix(self.y, predictions)
            print(confusion_matrix(predictions, self.y))
            print(classification_report(self.y, predictions, digits=2))

            print_confusion_matrix(
                self.y,
                predictions,
                "Confusion Matrix based on whole data set",
            )
        
        if self.settings.test_split and self.settings.output:
            split_model = LogisticRegression(
                solver='lbfgs',
                random_state=0,
                class_weight='balanced',
                max_iter=10000
            )

            run_split_test(self.array_scores, self.y, split_model, extended=True)

    def predict(self, x_sample: pd.DataFrame):
        '''Performs LR prediction once the model is trained.'''
        if self.model is None:
            raise RuntimeError("The LR model is not trained yet!")

        prediction = self.model.predict(x_sample)
        probabilities = self.model.predict_proba(x_sample)

        if self.settings.output:
            print(prediction)
            print(probabilities)

        return prediction
