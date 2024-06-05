'''Support Vector Machine module.'''
from copy import copy
from typing import Optional

import pandas as pd

from sklearn.svm import SVC

from chemfusekit.lldf import LLDFDataModel
from chemfusekit.__utils import GraphMode, run_split_test, print_confusion_matrix
from .__base import BaseSettings, BaseClassifier, BaseDataModel


class SVMSettings(BaseSettings):
    '''Holds the settings for the SVM object.'''
    def __init__(self, kernel: str = 'linear', output: GraphMode = GraphMode.NONE, test_split: bool = False):
        super().__init__(output, test_split)
        if kernel not in ['linear', 'poly', 'gaussian', 'sigmoid']:
            raise ValueError("Invalid type: must be linear, poly, gaussian or sigmoid")
        self.kernel = kernel


class SVM(BaseClassifier):
    '''Class for Support Vector Machine analysis of the data'''
    def __init__(self, settings: SVMSettings, data: BaseDataModel):
        super().__init__(settings, data)

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

        svm_model.fit(self.data.x_data, self.data.y)
        self.model = svm_model

        predictions = svm_model.predict(self.data.x_data)
        print_confusion_matrix(
            self.data.y,
            predictions,
            "Confusion matrix based on the whole data set",
            mode=self.settings.output
        )

        if self.settings.test_split:
            run_split_test(
                x=self.data.x_data,
                y=self.data.y,
                model=SVC(kernel=self.settings.kernel),
                mode=self.settings.output
            )

    def import_model(self, import_path: str):
        model_backup = copy(self.model)
        super().import_model(import_path)
        if not isinstance(self.model, SVC):
            self.model = model_backup
            raise ImportError("The file you tried to import is not an SVC classifier.")
        self.settings.kernel = self.model.kernel
