'''k-Nearest Neighbors Analysis module'''
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report

import seaborn as sns
import matplotlib.pyplot as plt

from chemfusekit.lldf import LLDFModel

class KNNSettings:
    '''Holds the settings for the kNN object.'''
    def __init__(
            self,
            n_neighbors=15,
            metric='euclidean',
            weights='uniform',
            algorithm='auto',
            output=False,
            test_split=False
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
        if type(output) is not bool:
            print(type(output))
            raise TypeError("Invalid output: should be a boolean value.")
        if type(test_split) is not bool:
            raise TypeError("Invalid test_split: should be a boolean value.")
        if test_split is True and output is False:
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
    def __init__(self, settings, fused_data):
        if type(settings) is not KNNSettings:
            raise TypeError("Invalid settings: should be a KNNSettings-class object.")
        if type(fused_data) is not LLDFModel:
            raise TypeError("Invalid fused_data: shold be a LLDFModel-class object.")
        self.settings = settings
        self.fused_data = fused_data
        self.model = None

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

        if self.settings.output:
            # View the prediction on the test data
            y_pred = knn.predict(self.fused_data.x_data)
            print(y_pred)

            # Assuming 'y_true' and 'y_pred' are your true and predicted labels
            cm = confusion_matrix(self.fused_data.y, y_pred)

            # Get unique class labels from y_true
            class_labels = sorted(set(self.fused_data.y))

            # Plot the confusion matrix using seaborn with custom colormap (Blues)
            sns.heatmap(
                cm,
                annot=True,
                fmt='d',
                cmap='Blues',
                xticklabels=class_labels,
                yticklabels=class_labels,
                cbar=False, vmin=0,
                vmax=cm.max()
            )

            plt.xlabel('Predicted')
            plt.ylabel('True')
            plt.title('Confusion Matrix based on the whole data set')
            plt.show()

            # Print the classification report
            print(classification_report(self.fused_data.y, y_pred, digits=2))

        if self.settings.test_split and self.settings.output:
            # Split the data into a training set and a test set
            x_train, x_test, y_train, y_test = train_test_split(
                self.fused_data.x_data,
                self.fused_data.y,
                test_size=0.3,
                random_state=42
            )

            # Train the kNN model on the training section of the dataset
            knn = KNeighborsClassifier(
                n_neighbors=self.settings.n_neighbors,
                metric=self.settings.metric,
                weights=self.settings.weights,
                algorithm=self.settings.algorithm
            )
            knn.fit(x_train, y_train)

            # View the prediction on the test data
            y_pred = knn.predict(x_test)
            print(y_pred)

            # Assuming 'y_true' and 'y_pred' are your true and predicted labels
            cm = confusion_matrix(y_test, y_pred)

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
            print(classification_report(y_test, y_pred, digits=2))

    def predict(self, x_data):
        '''Performs kNN prediction once the model is trained.'''
        if x_data is None:
            raise TypeError("X data for kNN prediction must be non-empty.")
        if self.model is None:
            raise RuntimeError("The kNN model is not trained yet!")

        y_pred = self.model.predict(x_data)
        return y_pred
