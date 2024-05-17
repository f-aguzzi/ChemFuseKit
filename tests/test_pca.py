'''This module contains the test cases for the PCA module.'''
import unittest
from chemfusekit.pca import PCASettings, PCA
from chemfusekit.lldf import LLDFSettings, LLDF

class TestPCA(unittest.TestCase):
    '''Test suite for the PCA module.'''

    def test_pca_settings(self):
        '''Test case against settings errors.'''
        # Test for rejection of a negative variance:
        with self.assertRaises(ValueError):
            PCASettings(target_variance=-0.3)

        # Test for rejection of an out-of-bounds confidence level:
        with self.assertRaises(ValueError):
            PCASettings(confidence_level=3)

        # Test for rejection of insufficient initial components:
        with self.assertRaises(ValueError):
            PCASettings(initial_components=2)

        # Now try with no mistakes:
        PCASettings(
            target_variance=0.98,
            confidence_level=0.9,
            initial_components=8,
            output=True
        )

    def test_pca_constructor(self):
        '''Test case against constructor parameter issues.'''

        # Create a LLDF model and initialize it
        lldf_settings = LLDFSettings(
            qepas_path='tests/qepas.xlsx',
            qepas_sheet='Sheet1',
            rt_path='tests/rt.xlsx',
            rt_sheet='Sheet1',
            preprocessing='snv'
        )
        lldf = LLDF(lldf_settings)
        lldf.lldf()

        lda_settings = PCASettings()

        # First, construct the object with null model:
        with self.assertRaises(TypeError):
            PCA(None, lda_settings)

        # Then, construct the object with null settings:
        with self.assertRaises(TypeError):
            PCA(lldf.fused_data, None)

        # Now, with both null:
        with self.assertRaises(TypeError):
            PCA(None, None)

        # Finally, with proper values:
        PCA(lldf.fused_data, lda_settings)
    
    def test_pca(self):
        '''
        Integration test case to verify that the output does not change based on
        whether the output is set to true or false
        '''
        # Create a LLDF model and initialize it
        lldf_settings = LLDFSettings(
            qepas_path='tests/qepas.xlsx',
            qepas_sheet='Sheet1',
            rt_path='tests/rt.xlsx',
            rt_sheet='Sheet1',
            preprocessing='snv'
        )
        lldf = LLDF(lldf_settings)
        lldf.lldf()

        # Set up and execute PCA
        pca_settings = PCASettings(output=True)
        pca = PCA(lldf.fused_data, pca_settings)
        pca.pca()

        # Save the results
        result_true_components = pca.components
        result_true_array_scores = pca.array_scores

        # Set up and execute PCA (again)
        pca_settings = PCASettings(output=False)
        pca = PCA(lldf.fused_data, pca_settings)
        pca.pca()

       # Save the results
        result_false_components = pca.components
        result_false_array_scores = pca.array_scores

        self.assertEqual(result_true_components, result_false_components)
        self.assertEqual(result_true_array_scores, result_false_array_scores)
 