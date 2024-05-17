'''Support Vector Machine module.'''
import matplotlib.pyplot as plt
# matplotlib inline

import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.svm import SVC

class SVMSettings:
    '''Holds the settings for the SVM object.'''
    def __init__(self, kernel='linear', output=False):
        if kernel is None:
            raise TypeError("Kernel cannot be null.")
        if kernel not in ['linear', 'poly', 'gaussian', 'sigmoid']:
            raise ValueError("Invalid type: must be linear, poly, gaussian or sigmoid")
        if output is None:
            raise TypeError("Output selection cannot be null.")
        self.kernel = kernel
        self.output = output

class SVM:
    '''Class for Support Vector Machine analysis of the data'''
    def __init__(self, fused_data, settings):
        if fused_data is None:
            raise ValueError("Fused data input cannot be empty.")
        if settings is None:
            raise ValueError("Settings cannot be empty.")
        self.fused_data = fused_data
        self.settings = settings
        self.model = None

    def svm(self):
        '''Performs Support Vector Machine analysis'''

        x_data = self.fused_data.x_data
        x_train = self.fused_data.x_train
        y = self.fused_data.y

        x_train, x_test, y_train, y_test = train_test_split(
            x_data,
            y,
            train_size=0.7,
            shuffle=True,
            stratify=y
        )

        # Linear kernel
        if self.settings.kernel == 'linear':
            svm_model = SVC(kernel='linear', probability=True)
            # svmlinear.predict_proba(X_train)
        # Polynomial kernel
        elif self.settings.kernel == 'poly':
            svm_model = SVC(kernel='poly', degree=8)
        # Gaussian kernel - radial basis function
        elif self.settings.kernel == 'gaussian':
            svm_model = SVC(kernel='rbf')
        # Sigmoid classifier
        elif self.settings.kernel == 'sigmoid':
            svm_model = SVC(kernel='sigmoid')
        else:
            raise ValueError(f"SVM: this type of kernel does not exist ({self.settings.type=})")

        svm_model.fit(x_train, y_train)
        self.model = svm_model

        if self.settings.output:
            y_pred = svm_model.predict(x_test)

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
        '''Performs SVM prediction once the model is trained'''
        if self.model is None:
            raise RuntimeError("The model hasn't been trained yet!")
        if x_data is None:
            raise TypeError("X data for prediction cannot be empty.")

        return self.model.predict(x_data)
