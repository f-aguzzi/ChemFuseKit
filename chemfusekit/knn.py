'''k-Nearest Neighbors Analysis module'''
from typing import Optional
from beartype.typing import Callable

from sklearn.neighbors import KNeighborsClassifier

import pandas as pd

from chemfusekit.lldf import LLDFModel
from chemfusekit.__utils import run_split_test, print_confusion_matrix, print_table, GraphMode

class KNNSettings:
    '''Holds the settings for the kNN object.'''
    def __init__(
            self,
            n_neighbors: int = 15,
            metric: str | Callable = 'euclidean',
            weights: str | Callable = 'uniform',
            algorithm: str = 'auto',
            output: GraphMode = GraphMode.NONE,
            test_split: bool = False
        ):
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
        if test_split is True and output is GraphMode.NONE:
            raise Warning(
                "You selected test_split but it won't run because you disabled the output."
            )
        self.n_neighbors = n_neighbors
        self.metric = metric
        self.weights = weights
        self.algorithm = algorithm
        self.output = output
        self.test_split = test_split

class KNN:
    '''Class to store the data, methods and artifacts for k-Nearest Neighbors Analysis'''
    def __init__(self, settings: KNNSettings, fused_data: LLDFModel):
        self.settings = settings
        self.fused_data = fused_data
        self.model: Optional[KNeighborsClassifier] = None

    def knn(self):
        '''Performs k-Nearest Neighbors Analysis'''
        # Prepare and train the kNN model
        knn = KNeighborsClassifier(
            n_neighbors=self.settings.n_neighbors,
            metric=self.settings.metric,
            weights=self.settings.weights,
            algorithm=self.settings.algorithm
        )
        knn.fit(self.fused_data.x_data, self.fused_data.y)

        # Save the trained model
        self.model = knn

        # View the prediction on the test data
        y_pred = knn.predict(self.fused_data.x_data)
        print_table(
            ["Predictions"],
            y_pred.reshape(1,len(y_pred)),
            "Data and predictions",
            self.settings.output
        )

        print_confusion_matrix(
            self.fused_data.y,
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
            run_split_test(self.fused_data.x_data, self.fused_data.y, knn_split)


    def predict(self, x_data: pd.DataFrame):
        '''Performs kNN prediction once the model is trained.'''
        if x_data is None:
            raise TypeError("X data for kNN prediction must be non-empty.")
        if self.model is None:
            raise RuntimeError("The kNN model is not trained yet!")

        y_pred = self.model.predict(x_data)
        return y_pred
