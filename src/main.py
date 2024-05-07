import lldf
import pca
import svm

class Library:
    def __init__(self):
        self.LLDF = lldf.LLDF()
        self.LLDF.lldf()
        self.fused_data = self.LLDF.fused_data
        self.SVM = svm.SVM(self.fused_data)