'''This module contains the test cases for the LLDF module.'''
import unittest
from chemfusekit.lldf import LLDFSettings, LLDF

class TestLLDF(unittest.TestCase):
    '''Test suite for the LLDF module.'''

    def test_file_loading(self):
        '''Test case against file loading errors.'''
        # load a non-existent file on purpose
        settings = LLDFSettings(
            qepas_path='tests/notfound.xlsx',
            qepas_sheet='Sheet1',
            rt_path='tests/rtx.xlsx',
            rt_sheet='Sheet1',
            preprocessing='savgol'
        )
        lldf = LLDF(settings)
        self.assertRaises(FileNotFoundError, lldf.lldf)

    def test_preprocessing_techniques(self):
        '''Test case against wrong preprocessing user input.'''
        settings = LLDFSettings(
            qepas_path='tests/qepas.xlsx',
            qepas_sheet='Sheet1',
            rt_path='tests/rt.xlsx',
            rt_sheet='Sheet1',
            preprocessing='qpl' # test with non-existent preprocessing technique
        )
        lldf = LLDF(settings)
        self.assertRaises(SyntaxError, lldf.lldf)

        # now check if it works with the three real processing techniques:
        lldf.settings.preprocessing='snv'
        lldf.lldf()
        lldf.settings.preprocessing='savgol'
        lldf.lldf()
        lldf.settings.preprocessing='savgol+snv'
        lldf.lldf()
    
    def test_export(self):
        '''Test case against wrong export settings.'''
        settings = LLDFSettings(
            qepas_path='tests/qepas.xlsx',
            qepas_sheet='Sheet1',
            rt_path='tests/rt.xlsx',
            rt_sheet='Sheet1',
            preprocessing='snv' # test with non-existent preprocessing technique
        )
        lldf = LLDF(settings)
        
        # Try exporting data before data fusion
        with self.assertRaises(RuntimeError):
            lldf.export_data('path')

        # Perform data fusion
        lldf.lldf()

        # Try exporting data to an invalid path
        with self.assertRaises(RuntimeError):
            lldf.export_data('$£=0\//|') 

if __name__ == '__main__':
    unittest.main()
