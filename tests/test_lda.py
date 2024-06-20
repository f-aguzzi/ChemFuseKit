"""This module contains the test cases for the LDA module."""
import unittest
from chemfusekit.lda import LDASettings, LDA, GraphMode
from chemfusekit.df import DFSettings, DF, Table


class TestLDA(unittest.TestCase):
    """Test suite for the LDA module."""

    def test_lda_settings(self):
        """Test case against settings errors."""
        # Check for negative component rejection
        with self.assertRaises(ValueError):
            LDASettings(components=-3, output='text')
        # Check if split tests with no output cause warnings:
        with self.assertRaises(Warning):
            LDASettings(output='none', test_split=True)

    def test_lda_constructor(self):
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

        lda_settings = LDASettings()

        # First, construct the object with null model:
        with self.assertRaises(TypeError):
            LDA(lda_settings, None)

        # Then, construct the object with null settings:
        with self.assertRaises(TypeError):
            LDA(None, df.fused_data)

        # Now, with both null:
        with self.assertRaises(TypeError):
            LDA(None, None)

        # Finally, with proper values:
        LDA(lda_settings, df.fused_data)

    def test_lda(self):
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

        # Create an LDA object and train it, with graphical output
        lda_settings = LDASettings(output='graphical')
        lda = LDA(lda_settings, df.fused_data)
        lda.train()

        # Create an LDA object and train it, with text output
        lda_settings = LDASettings(output='text')
        lda = LDA(lda_settings, df.fused_data)
        lda.train()

        # Create an LDA object and train it, with no output
        lda_settings = LDASettings(output='none')
        lda = LDA(lda_settings, df.fused_data)
        lda.train()

        # Create an LDA object and train it, with true output and split tests
        lda_settings = LDASettings(output='text', test_split=True)
        lda = LDA(lda_settings, df.fused_data)
        lda.train()

    def test_lda_predict(self):
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

        # Create an LDA object without training it
        lda_settings = LDASettings()
        lda = LDA(lda_settings, df.fused_data)

        # Pick a random sample for prediction
        x_data_sample = df.fused_data.x_train.iloc[119]  # should be DMMP
        x_data_sample = x_data_sample.iloc[1:].to_frame().transpose()

        # Run prediction with untrained model (should throw exception)
        with self.assertRaises(RuntimeError):
            lda.predict(x_data_sample)

        # Train the LDA object
        lda.train()

        # Run prediction with empty data (should throw exception)
        with self.assertRaises(TypeError):
            lda.predict(None)

        # Run prediction with trained model and non-null data
        lda.predict(x_data_sample)
