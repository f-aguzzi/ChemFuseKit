"""This module contains the test cases for the LR module."""
import unittest

import numpy as np
import pandas as pd

from chemfusekit.df import DFSettings, DF, Table
from chemfusekit.pca import PCASettings, PCA
from chemfusekit.lr import LRSettings, LR
from chemfusekit.__base import ReducerDataModel


class TestLR(unittest.TestCase):
    """Test suite for the LR module."""

    def test_lr_settings(self):
        """Test case against settings input errors."""
        # Should raise an exception when the algorithm is not available
        with self.assertRaises(ValueError):
            LRSettings(
                algorithm='unknown',
                output='none',
                test_split=False
            )

        # Should raise an exception when any of the inputs is a null value
        with self.assertRaises(TypeError):
            LRSettings(
                algorithm=None,
                output='none',
                test_split=True
            )
        with self.assertRaises(TypeError):
            LRSettings(
                algorithm='liblinear',
                output=None,
                test_split=False
            )
        with self.assertRaises(TypeError):
            LRSettings(
                algorithm='liblinear',
                output='none',
                test_split=None
            )

        # Check if split tests with no output cause warnings:
        with self.assertRaises(Warning):
            LRSettings(output='none', test_split=True)

        # Should not raise any exception when the input is correct
        LRSettings(
            algorithm='liblinear',
            output='text'
        )

    def test_lr_constructor(self):
        """Test case against constructor input errors."""
        data_model = ReducerDataModel(
            x_data=pd.DataFrame([21.0, 3.44, 7.65]),
            x_train=pd.DataFrame(),
            y=np.asarray([7.854, 1.543, 93.55]),
            components=5
        )
        # Should raise an exception when the inputs are null
        with self.assertRaises(TypeError):
            LR(
                settings=None,
                data=data_model
            )
        with self.assertRaises(TypeError):
            LR(
                settings=LRSettings(),
                data=None
            )

        # Should not raise any exception when all inputs are valid
        LR(
            settings=LRSettings(),
            data=data_model
        )

    def test_lr(self):
        """Integration test case for LR training."""
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

        pca_settings = PCASettings()
        pca = PCA(pca_settings, df.fused_data)
        pca.train()
        pca.pca_stats()

        pca_data = pca.export_data()

        # With no output
        lr_settings = LRSettings()
        lr = LR(lr_settings, pca_data)
        lr.train()

        # With text output
        lr_settings = LRSettings(output='text')
        lr = LR(lr_settings, pca_data)
        lr.train()

        # With graph output
        # With text output
        lr_settings = LRSettings(output='graphical')
        lr = LR(lr_settings, pca_data)
        lr.train()

        # With text output and split tests
        lr_settings = LRSettings(output='text', test_split=True)
        lr = LR(lr_settings, pca_data)
        lr.train()

        # With graph output and split tests
        lr_settings = LRSettings(output='graphical', test_split=True)
        lr = LR(lr_settings, pca_data)
        lr.train()

        # A final test with just the df data:
        lr_settings = LRSettings()
        lr = LR(lr_settings, df.fused_data)
        lr.train()

    def test_lr_predict(self):
        """Test case against prediction input errors."""
        # Set up the model
        lr_settings = LRSettings()
        pca_data = ReducerDataModel(
            x_data=pd.DataFrame([43.1, 0.06]),
            x_train=pd.DataFrame(),
            y=np.asarray([7.02, 8.11]),
            components=4
        )
        lr = LR(lr_settings, pca_data)

        # Shold raise an exception when started with no data
        with self.assertRaises(TypeError):
            lr.predict(None)

        # Should raise an exception when started with no training
        with self.assertRaises(RuntimeError):
            lr.predict(pd.DataFrame([4.03, 3.14]))
