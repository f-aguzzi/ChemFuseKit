import matplotlib.pyplot as plt
# matplotlib inline

import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.svm import SVC

class SVM:
    def __init__(self, fused_data):
            self.fused_data = fused_data

    def svm(self, type="linear"):
        self.settings.type = type

        X_data = self.fused_data.X_data
        X_train = self.fused_data.X_train
        Y = self.fused_data.Y

        X_train, X_test, y_train, y_test = train_test_split(X_data, Y, train_size=0.7, shuffle=True, stratify=Y)

        # Linear kernel
        if self.settings.type == "linear":
            svm_model = SVC(kernel='linear', probability=True)
            # svmlinear.predict_proba(X_train)
        # Polynomial kernel
        elif self.settings.type == "poly":
            svm_model = SVC(kernel='poly', degree=8)
        # Gaussian kernel - radial basis function
        elif self.settings.type == "gaussian":
            svm_model = SVC(kernel='rbf')
        # Sigmoid classifier
        elif self.settings.type == "sigmoid":
            svm_model = SVC(kernel='sigmoid')
        else:
            raise Exception(f"SVM: this type of kernel does not exist ({self.settings.type=})")
        
        svm_model.fit(X_train, y_train)
        y_pred = svm_model.predict(X_test)

        # Assuming 'y_true' and 'y_pred' are your true and predicted labels
        cm = confusion_matrix(y_test, y_pred)

        # Get unique class labels from y_true
        class_labels = sorted(set(y_test))

        # Plot the confusion matrix using seaborn with custom colormap (Blues)
        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=class_labels, yticklabels=class_labels, cbar=False, vmin=0, vmax=cm.max())

        plt.xlabel('Predicted')
        plt.ylabel('True')
        plt.title('Confusion Matrix based on evaluation set')
        plt.show()

        # Print the classification report
        print(classification_report(y_test, y_pred, digits=2))