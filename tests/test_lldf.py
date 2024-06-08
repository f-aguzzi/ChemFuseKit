'''This module contains the test cases for the LLDF module.'''
import unittest
from chemfusekit.lldf import LLDFSettings, LLDF, GraphMode, Table

class TestLLDF(unittest.TestCase):
    '''Test suite for the LLDF module.'''

    def test_file_loading(self):
        '''Test case against file loading errors.'''
        # load a non-existent file on purpose
        settings = LLDFSettings(
            output=GraphMode.NONE
        )

        table1 = Table(
            file_path='tests/nonexistent.xlsx',
            sheet_name='Sheet1',
            preprocessing='none'
        )

        files = [table1]
        lldf = LLDF(settings=settings, tables=files)
        self.assertRaises(FileNotFoundError, lldf.lldf)

    def test_preprocessing_techniques(self):
        '''Test case against wrong preprocessing user input.'''
        with self.assertRaises(SyntaxError):
            settings = LLDFSettings(
                output=GraphMode.NONE
            )

            table1 = Table(
                file_path='tests/qepas.xlsx',
                sheet_name='Sheet1',
                preprocessing='qpl'
            )

            lldf = LLDF(settings, [table1])
            lldf.lldf()

        # Now a correct value:
        settings = LLDFSettings(output=GraphMode.NONE)
        table1 = Table(
            file_path='tests/qepas.xlsx',
            sheet_name='Sheet1',
            preprocessing='snv'
        )
        lldf = LLDF(settings, [table1])
        lldf.lldf()
    
    def test_export(self):
        '''Test case against wrong export settings.'''
        settings = LLDFSettings(output=GraphMode.NONE)
        table1 = Table(
            file_path='tests/qepas.xlsx',
            sheet_name='Sheet1',
            preprocessing='snv'
        )
        lldf = LLDF(settings, [table1])
        
        # Try exporting data before data fusion
        with self.assertRaises(RuntimeError):
            lldf.export_data('path')

        # Perform data fusion
        lldf.lldf()

        # Try exporting data to an invalid path
        with self.assertRaises(ValueError):
            lldf.export_data('$£=0\//|') 

if __name__ == '__main__':
    unittest.main()
