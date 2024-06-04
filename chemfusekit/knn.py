'''k-Nearest Neighbors Analysis module'''
from typing import Optional
from beartype.typing import Callable

from sklearn.neighbors import KNeighborsClassifier

import pandas as pd

from chemfusekit.lldf import LLDFDataModel
from chemfusekit.__utils import run_split_test, print_confusion_matrix, print_table, GraphMode
from .__base import BaseSettings, BaseClassifier


class KNNSettings(BaseSettings):
    '''Holds the settings for the kNN object.'''
    def __init__(self, n_neighbors: int = 15, metric: str | Callable = 'euclidean', weights: str | Callable = 'uniform',
                 algorithm: str = 'auto', output: GraphMode = GraphMode.NONE, test_split: bool = False):

        super().__init__(output, test_split)

        if n_neighbors < 1:
            raise ValueError("Invalid n_neighbors number: should be a positive integer.")
        if metric not in ['minkwoski', 'precomputed', 'euclidean'] and not callable(metric):
            raise ValueError(
                "Invalid metric: should be 'minkwoski', 'precomputed', 'euclidean' or a callable."
            )
        if weights not in ['uniform', 'distance'] and not callable(weights):
            raise ValueError("Invalid weight: should be 'uniform', 'distance' or a callable")
        if algorithm not in ['auto', 'ball_tree', 'kd_tree', 'brute']:
            raise  ValueError(
                "Invalid algorithm: should be 'auto', 'ball_tree', 'kd_tree' or 'brute'."
            )
        self.n_neighbors = n_neighbors
        self.metric = metric
        self.weights = weights
        self.algorithm = algorithm


class KNN(BaseClassifier):
    '''Class to store the data, methods and artifacts for k-Nearest Neighbors Analysis'''
    def __init__(self, settings: KNNSettings, fused_data: LLDFDataModel):
        super().__init__(settings, fused_data)

    def knn(self):
        '''Performs k-Nearest Neighbors Analysis'''
        # Prepare and train the kNN model
        knn = KNeighborsClassifier(
            n_neighbors=self.settings.n_neighbors,
            metric=self.settings.metric,
            weights=self.settings.weights,
            algorithm=self.settings.algorithm
        )
        knn.fit(self.data.x_data, self.data.y)

        # Save the trained model
        self.model = knn

        # View the prediction on the test data
        y_pred = knn.predict(self.data.x_data)
        print_table(
            ["Predictions"],
            y_pred.reshape(1,len(y_pred)),
            "Data and predictions",
            self.settings.output
        )

        print_confusion_matrix(
            self.data.y,
            y_pred,
            "Confusion Matrix based on the whole data set",
            self.settings.output
        )

        if self.settings.test_split and self.settings.output:
            knn_split = KNeighborsClassifier(
                n_neighbors=self.settings.n_neighbors,
                metric=self.settings.metric,
                weights=self.settings.weights,
                algorithm=self.settings.algorithm
            )
            run_split_test(self.data.x_data, self.data.y, knn_split)

    def predict(self, x_data: pd.DataFrame):
        '''Performs kNN prediction once the model is trained.'''
        if x_data is None:
            raise TypeError("X data for kNN prediction must be non-empty.")
        if self.model is None:
            raise RuntimeError("The kNN model is not trained yet!")

        y_pred = self.model.predict(x_data)
        return y_pred