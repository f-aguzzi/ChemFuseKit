"""This module contains the test cases for the base module."""
import unittest

import os

import numpy as np

from chemfusekit.df import DFSettings, DF, Table
from chemfusekit._base import BaseDataModel
from chemfusekit.lda import LDASettings, LDA


class TestBase(unittest.TestCase):
    def test_import_export(self):
        """Test case for table import and export."""

        # Import and fuse data from tables
        df_settings = DFSettings()
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
        tables = [table1, table2]
        df = DF(df_settings, tables)
        df.fuse()

        # Export the fused dataset to file
        df.export_data("export_test.xlsx")

        # Import the fused dataset from file
        imported_data = BaseDataModel.load_from_file("export_test.xlsx", "Sheet1")

        # Assert the equality between the fused data and the export/import data
        # Compare the DataFrames using numpy.allclose()
        tolerance = 1e-6
        self.assertTrue(
            # Compare the DataFrames using numpy.allclose(): true if they match within tolerance
            np.allclose(df.fused_data.x_data.values, imported_data.x_data.values, atol=tolerance)
        )
        self.assertTrue(
            # The comparison between ndarrays returns an array of booleans, collapsed by "all()"
            (df.fused_data.y == imported_data.y).all()
        )

        # Second phase: re-export and re-import from BaseDataModel
        imported_data.export_to_file("export_test_2.xlsx")
        reimported_data = BaseDataModel.load_from_file("export_test_2.xlsx")

        # Assert the equality between the re-exported data and the re-reimported data
        self.assertTrue(np.allclose(df.fused_data.x_data.values, imported_data.x_data.values, atol=tolerance))
        self.assertTrue((df.fused_data.y == reimported_data.y).all())

        # Clean up
        os.remove("export_test.xlsx")
        os.remove("export_test_2.xlsx")

    def test_model_import(self):
        """Integration test for model dumping and reloading."""
        # Let's start by creating and training an LDA model
        lldf_settings = DFSettings()
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
        tables = [table1, table2]
        df = DF(lldf_settings, tables)
        df.fuse()
        lda_settings = LDASettings()
        lda = LDA(lda_settings, df.fused_data)
        lda.train()

        # Dump the model to file
        lda.export_model("modelfile.sklearn")

        # Reload the model
        lda2 = LDA(lda_settings, df.fused_data)
        lda2.import_model("modelfile.sklearn")

        # Check whether the imported model is the same as the exported model
        self.assertEqual(lda.model.get_params(), lda2.model.get_params())

        # Clean up
        os.remove("modelfile.sklearn")

    def test_from_file(self):
        """Test case for classifier import from file"""
        '''Integration test for model dumping and reloading.'''
        # Let's start by creating and training an LDA model
        df_settings = DFSettings()
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
        tables = [table1, table2]
        df = DF(df_settings, tables)
        df.fuse()
        lda_settings = LDASettings()
        lda = LDA(lda_settings, df.fused_data)
        lda.train()

        # Dump the model to file
        lda.export_model("modelfile.sklearn")

        lda2 = LDA.from_file(lda_settings, "modelfile.sklearn")

        # Check whether the imported model is the same as the exported model
        self.assertEqual(lda.model.get_params(), lda2.model.get_params())

        # Clean up
        os.remove("modelfile.sklearn")


if __name__ == '__main__':
    unittest.main()
