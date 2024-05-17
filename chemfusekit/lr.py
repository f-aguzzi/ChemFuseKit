'''Logistic Regression Module'''
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.model_selection import train_test_split
import seaborn as sns
import matplotlib.pyplot as plt

class LRSettings:
    '''Holds the settings for the LR object.'''
    def __init__(self, algorithm='liblinear', output=False):
        if algorithm is None:
            raise TypeError("The algorithm cannot be null.")
        if output is None:
            raise TypeError("The output selector cannot be null.")
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
        self.output = output

class LR:
    '''Class to store the data, methods and artifacts for Logistic Regression'''
    def __init__(self, settings, array_scores, y):
        if settings is None:
            raise TypeError("Settings cannot be null.")
        if array_scores is None:
            raise TypeError("Array scores cannot be null.")
        if y is None:
            raise TypeError("Y cannot be null.")
        self.settings = settings
        self.array_scores = array_scores
        self.y = y
        self.model = None

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

            # Assuming 'y_true' and 'y_pred' are your true and predicted labels
            cm = confusion_matrix(self.y, predictions)

            # Get unique class labels from y_true
            class_labels = sorted(set(self.y))

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
            plt.title('Confusion Matrix based on whole data set')
            plt.show()

            # Print the classification report
            print(classification_report(self.y, predictions, digits=2))

        # Split the data set int training set and evaluation set
        x_train, x_test, y_train, y_test = train_test_split(
            self.array_scores,
            self.y,
            train_size=0.7,
            shuffle=True,
            stratify=self.y
        )

        model = LogisticRegression(
            solver='lbfgs',
            random_state=0,
            class_weight='balanced',
            max_iter=10000
        ).fit(x_train, y_train)

        if self.settings.output:
            # we can see the classes the model used
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

        # This tells us the accuracy of our model in calibration
        model.score(x_train, y_train)

        predictions = model.predict(x_train)

        if self.settings.output:
            print("Calibration predictions: ")
            print(predictions)


            # Assuming 'y_true' and 'y_pred' are your true and predicted labels
            cm = confusion_matrix(y_train, predictions)

            # Get unique class labels from y_true
            class_labels = sorted(set(y_train))

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
            plt.title('Confusion Matrix based on training set')
            plt.show()

            # Print the classification report
            print(model.predict(x_test))

            # This tells us the accuracy of our model in calibration
            print(model.score(x_test, y_test))

            predictions = model.predict(x_test)
            cm = confusion_matrix(y_test, predictions)

            # Assuming 'y_true' and 'y_pred' are your true and predicted labels
            cm = confusion_matrix(y_test, predictions)

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
            print(classification_report(y_test, predictions, digits=2))

    def predict(self, x_sample):
        '''Performs LR prediction once the model is trained.'''   
        if x_sample is None:
            raise TypeError("Cannot classify a null sample.")
        if self.model is None:
            raise RuntimeError("The LR model is not trained yet!")

        prediction = self.model.predict(x_sample)
        probabilities = self.model.predict_proba(x_sample)

        if self.settings.output:
            print(prediction)
            print(probabilities)

        return prediction
