'''This module contains the test cases for the SVM module.'''
import unittest
from chemfusekit.svm import SVMSettings, SVM, GraphMode
from chemfusekit.lldf import LLDFSettings, LLDF

class TestSVM(unittest.TestCase):
    '''Test suite for the LDA module.'''

    def test_svm_settings(self):
        '''Test case against settings errors.'''
        # Test against null type
        with self.assertRaises(TypeError):
            SVMSettings(None, GraphMode.NONE, False)
        # Test against null output selector
        with self.assertRaises(TypeError):
            SVMSettings('linear', None, False)
        # Test against null test_split selector
        with self.assertRaises(TypeError):
            SVMSettings('linear', GraphMode.NONE, None)
        # Test against non-existent kernels
        with self.assertRaises(ValueError):
            SVMSettings('non-existent', GraphMode.NONE, False)

        # Check if split tests with no output cause warnings:
        with self.assertRaises(Warning):
            SVMSettings(output=GraphMode.NONE, test_split=True)

        # Now call with proper values:
        SVMSettings(kernel='gaussian', output=GraphMode.GRAPHIC, test_split=False)

    def test_svm_constructor(self):
        '''Test case against constructor parameter issues.'''

        # Create an LLDF model and initialize it
        lldf_settings = LLDFSettings(
            qepas_path='tests/qepas.xlsx',
            qepas_sheet='Sheet1',
            rt_path='tests/rt.xlsx',
            rt_sheet='Sheet1',
            preprocessing='snv'
        )
        lldf = LLDF(lldf_settings)
        lldf.lldf()

        svm_settings = SVMSettings()

        # First, construct the object with null model:
        with self.assertRaises(TypeError):
            SVM(None, svm_settings)

        # Then, construct the object with null settings:
        with self.assertRaises(TypeError):
            SVM(lldf.fused_data, None)

        # Now, with both null:
        with self.assertRaises(TypeError):
            SVM(None, None)

        # Finally, with proper values:
        SVM(lldf.fused_data, svm_settings)
    
    def test_svm(self):
        '''Integration test case.'''

        # Create an LLDF model and initialize it
        lldf_settings = LLDFSettings(
            qepas_path='tests/qepas.xlsx',
            qepas_sheet='Sheet1',
            rt_path='tests/rt.xlsx',
            rt_sheet='Sheet1',
            preprocessing='snv'
        )
        lldf = LLDF(lldf_settings)
        lldf.lldf()

        # Create an SVM object and train it, with no output
        svm_settings = SVMSettings(output=GraphMode.NONE)
        svm = SVM(lldf.fused_data, svm_settings)
        svm.svm()

        # Create an SVM object and train it, with graphical output
        svm_settings = SVMSettings(output=GraphMode.GRAPHIC)
        svm = SVM(lldf.fused_data, svm_settings)
        svm.svm()

        # Create an SVM object and train it, with text output
        svm_settings = SVMSettings(output=GraphMode.TEXT)
        svm = SVM(lldf.fused_data, svm_settings)
        svm.svm()

    def test_svm_predict(self):
        '''Test case against prediction parameter issues.'''        

        # Create an LLDF model and initialize it
        lldf_settings = LLDFSettings(
            qepas_path='tests/qepas.xlsx',
            qepas_sheet='Sheet1',
            rt_path='tests/rt.xlsx',
            rt_sheet='Sheet1',
            preprocessing='snv'
        )
        lldf = LLDF(lldf_settings)
        lldf.lldf()

        # Create an SVM object without training it
        svm_settings = SVMSettings()
        svm = SVM(lldf.fused_data, svm_settings)

        # Pick a random sample for prediction
        x_data_sample = lldf.fused_data.x_train.iloc[119] # should be DMMP
        x_data_sample = x_data_sample.iloc[1:].to_frame().transpose()

        # Run prediction with untrained model (should throw exception)
        with self.assertRaises(RuntimeError):
            svm.predict(x_data_sample)

        # Train the SVM object
        svm.svm()

        # Run prediction with empty data (should throw exception)
        with self.assertRaises(TypeError):
            svm.predict(None)

        # Run prediction with trained model and non-null data
        svm.predict(x_data_sample)
