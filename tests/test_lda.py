'''This module contains the test cases for the LDA module.'''
import unittest
from chemfusekit.lda import LDASettings, LDA
from chemfusekit.lldf import LLDFSettings, LLDF

class TestLDA(unittest.TestCase):
    '''Test suite for the LDA module.'''

    def test_lda_settings(self):
        '''Test case against settings errors.'''
        with self.assertRaises(ValueError):
            LDASettings(components=-3, output=True)

    def test_lda_constructor(self):
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

        lda_settings = LDASettings()

        # First, construct the object with null model:
        with self.assertRaises(TypeError):
            LDA(None, lda_settings)

        # Then, construct the object with null settings:
        with self.assertRaises(TypeError):
            LDA(lldf.fused_data, None)

        # Now, with both null:
        with self.assertRaises(TypeError):
            LDA(None, None)

        # Finally, with proper values:
        LDA(lldf.fused_data, lda_settings)
    
    def test_lda(self):
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

        # Create an LDA object and train it, with true output
        lda_settings = LDASettings(output=True)
        lda = LDA(lldf.fused_data, lda_settings)
        lda.lda()

        # Create an LDA object and train it, with false output
        lda_settings = LDASettings(output=False)
        lda = LDA(lldf.fused_data, lda_settings)
        lda.lda()

    def test_lda_predict(self):
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

        # Create an LDA object without training it
        lda_settings = LDASettings()
        lda = LDA(lldf.fused_data, lda_settings)

        # Pick a random sample for prediction
        x_data_sample = lldf.fused_data.x_train.iloc[119] # should be DMMP
        x_data_sample = x_data_sample.iloc[1:].to_frame().transpose()

        # Run prediction with untrained model (should throw exception)
        with self.assertRaises(RuntimeError):
            lda.predict(x_data_sample)

        # Train the LDA object
        lda.lda()

        # Run prediction with empty data (should throw exception)
        with self.assertRaises(TypeError):
            lda.predict(None)

        # Run prediction with trained model and non-null data
        lda.predict(x_data_sample)
