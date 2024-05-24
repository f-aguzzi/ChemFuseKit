'''Support Vector Machine module.'''
from typing import Optional

import pandas as pd

from sklearn.svm import SVC

from chemfusekit.lldf import LLDFModel
from chemfusekit.__utils import GraphMode, run_split_test, print_confusion_matrix



class SVMSettings:
    '''Holds the settings for the SVM object.'''
    def __init__(self, kernel: str = 'linear', output: GraphMode = GraphMode.NONE,
                 test_split: bool = False):
        if kernel not in ['linear', 'poly', 'gaussian', 'sigmoid']:
            raise ValueError("Invalid type: must be linear, poly, gaussian or sigmoid")
        if test_split is True and output is GraphMode.NONE:
            raise Warning(
                "You selected test_split but it won't run because you disabled the output."
            )
        self.kernel = kernel
        self.output = output
        self.test_split = test_split


class SVM:
    '''Class for Support Vector Machine analysis of the data'''
    def __init__(self, fused_data: LLDFModel, settings: SVMSettings):
        self.fused_data = fused_data
        self.settings = settings
        self.model: Optional[SVC] = None


    def svm(self):
        '''Performs Support Vector Machine analysis'''

        # Linear kernel
        if self.settings.kernel == 'linear':
            svm_model = SVC(kernel='linear', probability=True)
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
            raise ValueError(f"SVM: this type of kernel does not exist ({self.settings.kernel=})")

        svm_model.fit(self.fused_data.x_data, self.fused_data.y)
        self.model = svm_model

        predictions = svm_model.predict(self.fused_data.x_data)
        print_confusion_matrix(
            self.fused_data.y,
            predictions,
            "Confusion matrix based on the whole data set",
            mode=self.settings.output
        )

        if self.settings.test_split:
            run_split_test(
                x=self.fused_data.x_data,
                y=self.fused_data.y,
                model=SVC(kernel=self.settings.kernel),
                mode=self.settings.output
            )


    def predict(self, x_data: pd.DataFrame):
        '''Performs SVM prediction once the model is trained'''
        if self.model is None:
            raise RuntimeError("The model hasn't been trained yet!")
        if x_data is None:
            raise TypeError("X data for prediction cannot be empty.")

        return self.model.predict(x_data)
