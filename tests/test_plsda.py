'''This module contains the test cases for the KNN module.'''
import unittest

import numpy as np
import pandas as pd

from chemfusekit.plsda import PLSDASettings, PLSDA, GraphMode
from chemfusekit.lldf import LLDFSettings, LLDF, LLDFDataModel, Table


class TestPLSDA(unittest.TestCase):
    '''Test suite for the PLSDA module.'''

    def test_plsda_settings(self):
        '''Test case against settings errors.'''

        # n_components parameter
        with self.assertRaises(ValueError):
            PLSDASettings(n_components=-3) # Negative value
        with self.assertRaises(ValueError):
            PLSDASettings(n_components=0)  # Zero value
        PLSDASettings(n_components=7)  # Correct value (shouldn't raise anything)

        # output parameter
        with self.assertRaises(TypeError):
            PLSDASettings(output=3)   # Wrong type (not a bool)

        # test_split parameter
        with self.assertRaises(TypeError):
            PLSDASettings(test_split=3)   # Wrong type (not a bool)

        # output and test_split incompatibilities
        with self.assertRaises(Warning):
            PLSDASettings(output=GraphMode.NONE, test_split=True)

    def test_plsda_constructor(self):
        '''Test case against constructor errors.'''
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

        # settings parameter
        wrong_settings = LLDFDataModel(pd.DataFrame([1]), pd.DataFrame([1]), np.asarray([1]))
        with self.assertRaises(TypeError):
            PLSDA(wrong_settings, lldf.fused_data)  # pass an object of the wrong class as settings

        # fused_data parameter
        knn_settings = PLSDASettings()
        wrong_fused_data = lldf_settings
        with self.assertRaises(TypeError):
            PLSDA(knn_settings, wrong_fused_data)  # pass an object of the wrong class as fused_data
    
    def test_plsda(self):
        '''Integration test case for the training function.'''
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

        # Set up and run PLSDA (no output)
        plsda_settings = PLSDASettings()
        plsda = PLSDA(plsda_settings, lldf.fused_data)
        plsda.plsda()

        # Set up and run PLSDA with text output
        plsda_settings = PLSDASettings(output=GraphMode.TEXT)
        plsda = PLSDA(plsda_settings, lldf.fused_data)
        plsda.plsda()

        # Set up and run PLSDA with graphical output
        plsda_settings = PLSDASettings(output=GraphMode.GRAPHIC)
        plsda = PLSDA(plsda_settings, lldf.fused_data)
        plsda.plsda()

        # Run with text output and split testing
        plsda_settings = PLSDASettings(output=GraphMode.TEXT, test_split=True)
        plsda = PLSDA(plsda_settings, lldf.fused_data)
        plsda.plsda()

        # Run with graphical output and split testing
        plsda_settings = PLSDASettings(output=GraphMode.GRAPHIC, test_split=True)
        plsda = PLSDA(plsda_settings, lldf.fused_data)
        plsda.plsda() 
    
    def test_prediction(self):
        '''Test case against prediction parameter issues.'''
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

        # Set up KNN without training it
        plsda_settings = PLSDASettings()
        plsda = PLSDA(plsda_settings, lldf.fused_data)

        # Pick a random sample for prediction
        x_data_sample = lldf.fused_data.x_train.iloc[119] # should be DMMP
        x_data_sample = x_data_sample.iloc[1:].to_frame().transpose()

        # Run prediction with untrained model (should throw exception)
        with self.assertRaises(RuntimeError):
            plsda.predict(x_data_sample)

        # Run training
        plsda.plsda()

        # Run prediction with empty data (should throw exception)
        with self.assertRaises(TypeError):
            plsda.predict(None)

        # Run prediction with trained model and non-null data
        plsda.predict(x_data_sample)
