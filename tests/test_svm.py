"""This module contains the test cases for the SVM module."""
import unittest
from chemfusekit.svm import SVMSettings, SVM
from chemfusekit.df import DFSettings, DF, Table


class TestSVM(unittest.TestCase):
    """Test suite for the LDA module."""

    def test_svm_settings(self):
        """Test case against settings errors."""
        # Test against null type
        with self.assertRaises(TypeError):
            SVMSettings(None, 'none', False)
        # Test against null output selector
        with self.assertRaises(TypeError):
            SVMSettings('linear', None, False)
        # Test against null test_split selector
        with self.assertRaises(TypeError):
            SVMSettings('linear', 'none', None)
        # Test against non-existent kernels
        with self.assertRaises(ValueError):
            SVMSettings('non-existent', 'none', False)

        # Check if split tests with no output cause warnings:
        with self.assertRaises(Warning):
            SVMSettings(output='none', test_split=True)

        # Now call with proper values:
        SVMSettings(kernel='gaussian', output='graphical', test_split=False)

    def test_svm_constructor(self):
        """Test case against constructor parameter issues."""

        # Perform preliminary data fusion
        df_settings = DFSettings(output='none')
        table1 = Table(
            file_path="tests/qepas.xlsx",
            sheet_name="Sheet1",
            preprocessing="snv"
        )
        table2 = Table(
            file_path="tests/rt.xlsx",
            sheet_name="Sheet1",
            preprocessing="none"
        )
        df = DF(df_settings, [table1, table2])
        df.fuse()

        svm_settings = SVMSettings()

        # First, construct the object with null model:
        with self.assertRaises(TypeError):
            SVM(svm_settings, None)

        # Then, construct the object with null settings:
        with self.assertRaises(TypeError):
            SVM(None, df.fused_data)

        # Now, with both null:
        with self.assertRaises(TypeError):
            SVM(None, None)

        # Finally, with proper values:
        SVM(svm_settings, df.fused_data)

    def test_svm(self):
        """Integration test case."""

        # Perform preliminary data fusion
        df_settings = DFSettings(output='none')
        table1 = Table(
            file_path="tests/qepas.xlsx",
            sheet_name="Sheet1",
            preprocessing="snv"
        )
        table2 = Table(
            file_path="tests/rt.xlsx",
            sheet_name="Sheet1",
            preprocessing="none"
        )
        df = DF(df_settings, [table1, table2])
        df.fuse()

        # Create an SVM object and train it, with no output
        svm_settings = SVMSettings(output='none')
        svm = SVM(svm_settings, df.fused_data)
        svm.train()

        # Create an SVM object and train it, with graphical output
        svm_settings = SVMSettings(output='graphical')
        svm = SVM(svm_settings, df.fused_data)
        svm.train()

        # Create an SVM object and train it, with text output
        svm_settings = SVMSettings(output='text')
        svm = SVM(svm_settings, df.fused_data)
        svm.train()

    def test_svm_predict(self):
        """Test case against prediction parameter issues."""

        # Perform preliminary data fusion
        df_settings = DFSettings(output='none')
        table1 = Table(
            file_path="tests/qepas.xlsx",
            sheet_name="Sheet1",
            preprocessing="snv"
        )
        table2 = Table(
            file_path="tests/rt.xlsx",
            sheet_name="Sheet1",
            preprocessing="none"
        )
        df = DF(df_settings, [table1, table2])
        df.fuse()

        # Create an SVM object without training it
        svm_settings = SVMSettings()
        svm = SVM(svm_settings, df.fused_data)

        # Pick a random sample for prediction
        x_data_sample = df.fused_data.x_train.iloc[119]  # should be DMMP
        x_data_sample = x_data_sample.iloc[1:].to_frame().transpose()

        # Run prediction with untrained model (should throw exception)
        with self.assertRaises(RuntimeError):
            svm.predict(x_data_sample)

        # Train the SVM object
        svm.train()

        # Run prediction with empty data (should throw exception)
        with self.assertRaises(TypeError):
            svm.predict(None)

        # Run prediction with trained model and non-null data
        svm.predict(x_data_sample)
