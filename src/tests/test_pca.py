'''This module contains the test cases for the PCA module.'''
import unittest
from src.pca import PCASettings, PCA
from src.lldf import LLDFSettings, LLDF

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
            qepas_path='src/tests/qepas.xlsx',
            qepas_sheet='Sheet1',
            rt_path='src/tests/rt.xlsx',
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
