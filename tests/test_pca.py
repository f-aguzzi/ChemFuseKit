'''This module contains the test cases for the PCA module.'''
import unittest
import copy
from chemfusekit.pca import PCASettings, PCA, GraphMode
from chemfusekit.lldf import LLDFSettings, LLDF, Table
from chemfusekit.lr import LRSettings, LR

class TestPCA(unittest.TestCase):
    '''Test suite for the PCA module.'''

    def test_pca_settings(self):
        '''Test case against settings errors.'''
        # Test for rejection of a negative variance:
        with self.assertRaises(ValueError):
            PCASettings(target_variance=-0.3)

        # Test for rejection of an out-of-bounds confidence level:
        with self.assertRaises(ValueError):
            PCASettings(confidence_level=3.00)

        # Test for rejection of insufficient initial components:
        with self.assertRaises(ValueError):
            PCASettings(initial_components=2)

        # Now try with no mistakes:
        PCASettings(
            target_variance=0.98,
            confidence_level=0.9,
            initial_components=8,
            output=GraphMode.GRAPHIC
        )

    def test_pca_constructor(self):
        '''Test case against constructor parameter issues.'''

        # Perform preliminary data fusion
        lldf_settings = LLDFSettings(output=GraphMode.NONE)
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
        lldf = LLDF(lldf_settings, [table1, table2])
        lldf.lldf()

        lda_settings = PCASettings()

        # First, construct the object with null model:
        with self.assertRaises(TypeError):
            PCA(lda_settings, None)

        # Then, construct the object with null settings:
        with self.assertRaises(TypeError):
            PCA(None, lldf.fused_data)

        # Now, with both null:
        with self.assertRaises(TypeError):
            PCA(None, None)

        # Finally, with proper values:
        PCA(lda_settings, lldf.fused_data)
    
    def test_pca(self):
        '''
        Integration test case to verify that the output does not change based on
        whether the output is set to true or false
        '''
        # Perform preliminary data fusion
        lldf_settings = LLDFSettings(output=GraphMode.NONE)
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
        lldf = LLDF(lldf_settings, [table1, table2])
        lldf.lldf()

        # Set up and execute PCA (graph output)
        pca_settings = PCASettings(output=GraphMode.GRAPHIC)
        pca = PCA(pca_settings, lldf.fused_data)
        pca.pca()

        # Save the results
        result_true_components = copy.deepcopy(pca.components)
        result_true_array_scores = copy.deepcopy(pca.array_scores)

        # Set up and execute PCA (again)
        pca_settings = PCASettings(output=GraphMode.NONE)
        pca = PCA(pca_settings, lldf.fused_data)
        pca.pca()

        # Save the results
        result_false_components = pca.components
        result_false_array_scores = pca.array_scores

        self.assertEqual(result_true_components, result_false_components)
        self.assertEqual(result_true_array_scores, result_false_array_scores)

        # Set up and execute PCA (text output)
        pca_settings = PCASettings(output=GraphMode.GRAPHIC)
        pca = PCA(pca_settings, lldf.fused_data)
        pca.pca()

        # Save the results
        result_true_components = copy.deepcopy(pca.components)
        result_true_array_scores = copy.deepcopy(pca.array_scores)

        # Set up and execute PCA (again)
        pca_settings = PCASettings(output=GraphMode.NONE)
        pca = PCA(pca_settings, lldf.fused_data)
        pca.pca()

        # Save the results
        result_false_components = pca.components
        result_false_array_scores = pca.array_scores

        self.assertEqual(result_true_components, result_false_components)
        self.assertEqual(result_true_array_scores, result_false_array_scores)

    def test_pca_integration_lr(self):
        '''Integration test for PCA+LR'''

        # Perform preliminary data fusion
        lldf_settings = LLDFSettings(output=GraphMode.NONE)
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
        lldf = LLDF(lldf_settings, [table1, table2])
        lldf.lldf()

        # Set up PCA and get the rescaled_data property directly
        pca_settings = PCASettings()
        pca = PCA(pca_settings, lldf.fused_data)
        rescaled_data = pca.rescaled_data

        # Set up and execute LR
        lr_settings = LRSettings()
        lr = LR(lr_settings, rescaled_data)
        lr.lr()

    def test_pca_import_export(self):
        '''Test case for the import and export of PCA models.'''
        # Perform preliminary data fusion
        lldf_settings = LLDFSettings(output=GraphMode.NONE)
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
        lldf = LLDF(lldf_settings, [table1, table2])
        lldf.lldf()

        # Set up PCA
        pca_settings = PCASettings()
        pca = PCA(pca_settings, lldf.fused_data)

        # Try exporting the model before executing pca()
        with self.assertRaises(RuntimeError):
            pca.export_model('pca_model.sklearn')

        # Execute PCA and retry exporting
        pca.pca()
        pca.export_model('pca_model.sklearn')

        # Try creating a new PCA object from the wrong type of file
        with self.assertRaises(ImportError):
            PCA.from_file(pca_settings, 'tests/qepas.xlsx')

        # Create a new PCA object from file
        pca2 = PCA.from_file(pca_settings, 'pca_model.sklearn')

        # Assert the equality of the two models
        self.assertEqual(pca.pca_model.get_params(), pca2.pca_model.get_params())

    def test_pca_reduce(self):
        '''Test case for data dimensionality reduction.'''
        # Perform preliminary data fusion
        lldf_settings = LLDFSettings(output=GraphMode.NONE)
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
        lldf = LLDF(lldf_settings, [table1, table2])
        lldf.lldf()

        # Set up PCA
        pca_settings = PCASettings()
        pca = PCA(pca_settings, lldf.fused_data)

        # Try rescaling data before training the model
        with self.assertRaises(RuntimeError):
            pca.reduce(lldf.fused_data)

        # Execute PCA and then rescale
        pca.pca()
        reduced_data = pca.reduce(lldf.fused_data)

        # Check that the dimensionality (number of columns) is reduced
        self.assertLess(lldf.fused_data.x_data.shape[1], reduced_data.x_data.shape[1])
