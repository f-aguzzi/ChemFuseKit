"""This module contains the test cases for the LLDF module."""
import unittest
from chemfusekit.df import DFSettings, DF, GraphMode, Table


class TestLLDF(unittest.TestCase):
    """Test suite for the LLDF module."""

    def test_file_loading(self):
        """Test case against file loading errors."""
        # load a non-existent file on purpose
        settings = DFSettings(
            output=GraphMode.NONE
        )

        table1 = Table(
            file_path='tests/nonexistent.xlsx',
            sheet_name='Sheet1',
            preprocessing='none'
        )

        files = [table1]
        df = DF(settings=settings, tables=files)
        self.assertRaises(FileNotFoundError, df.fuse)

    def test_preprocessing_techniques(self):
        """Test case against wrong preprocessing user input."""
        with self.assertRaises(SyntaxError):
            settings = DFSettings(
                output=GraphMode.NONE
            )

            table1 = Table(
                file_path='tests/qepas.xlsx',
                sheet_name='Sheet1',
                preprocessing='qpl'
            )

            df = DF(settings, [table1])
            df.fuse()

        # Now a correct value:
        settings = DFSettings(output=GraphMode.NONE)
        table1 = Table(
            file_path='tests/qepas.xlsx',
            sheet_name='Sheet1',
            preprocessing='snv'
        )
        df = DF(settings, [table1])
        df.fuse()

    def test_export(self):
        """Test case against wrong export settings."""
        settings = DFSettings(output=GraphMode.NONE)
        table1 = Table(
            file_path='tests/qepas.xlsx',
            sheet_name='Sheet1',
            preprocessing='snv'
        )
        df = DF(settings, [table1])

        # Try exporting data before data fusion
        with self.assertRaises(RuntimeError):
            df.export_data('path')

        # Perform data fusion
        df.fuse()

        # Try exporting data to an invalid path
        with self.assertRaises(ValueError):
            df.export_data('$£=0\//|')


if __name__ == '__main__':
    unittest.main()
