'''This module contains the test cases for the LR module.'''
import unittest
from chemfusekit.lldf import LLDFSettings, LLDF
from chemfusekit.pca import PCASettings, PCA
from chemfusekit.lr import LRSettings, LR

class TestLR(unittest.TestCase):
    '''Test suite for the LR module.'''

    def test_lr_settings(self):
        '''Test case against settings input errors.'''
        # Should raise an exception when the algorithm is not available
        with self.assertRaises(ValueError):
            LRSettings(
                algorithm='unknown',
                output=True
            )

        # Should raise an exception when any of the inputs is a null value
        with self.assertRaises(TypeError):
            LRSettings(
                algorithm=None,
                output=True
            )
        with self.assertRaises(TypeError):
            LRSettings(
                algorithm='liblinear',
                output=None
            )
        with self.assertRaises(TypeError):
            LRSettings(
                algorithm=None,
                output=None
            )

        # Should not raise any exception when the input is correct
        LRSettings(
            algorithm='liblinear',
            output=False
        )

    def test_lr_constructor(self):
        '''Test case against constructor input errors.'''
        # Should raise an exception when the inputs are null
        with self.assertRaises(TypeError):
            LR(
                settings=None,
                array_scores=[21.0, 3.44, 7.65],
                y=[7.854, 1.543, 93.55]
            )
        with self.assertRaises(TypeError):
            LR(
                settings=LRSettings(),
                array_scores=None,
                y=[7.854, 1.543, 93.55]
            )
        with self.assertRaises(TypeError):
            LR(
                settings=LRSettings(),
                array_scores=[21.0, 3.44, 7.65],
                y=None
            )

        # Should not raise any exception when all inputs are valid
        LR(
            settings=LRSettings(),
            array_scores=[21.0, 3.44, 7.65],
            y=[7.854, 1.543, 93.55]
        )

    def test_lr(self):
        '''Integration test case for LR training.'''
        lldf_settings = LLDFSettings(
            qepas_path='tests/qepas.xlsx',
            qepas_sheet='Sheet1',
            rt_path='tests/rt.xlsx',
            rt_sheet='Sheet1',
            preprocessing='snv'
        )

        lldf = LLDF(lldf_settings)
        lldf.lldf()

        pca_settings = PCASettings()
        pca = PCA(lldf.fused_data, pca_settings)
        pca.pca()
        pca.pca_stats()

        lr_settings = LRSettings()
        lr = LR(lr_settings, pca.array_scores, lldf.fused_data.y)
        lr.lr()


    def test_lr_predict(self):
        '''Test case against prediction input errors.'''
        # Set up the model
        lr_settings = LRSettings()
        lr = LR(lr_settings, [7.02, 8.11], [43.1, 0.06])

        # Shold raise an exception when started with no data
        with self.assertRaises(TypeError):
            lr.predict(None)

        # Should raise an exception when started with no training
        with self.assertRaises(RuntimeError):
            lr.predict([4.03, 3.14])
