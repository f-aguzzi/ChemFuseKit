"""This module contains the test cases for the LLDF module."""
import unittest
from chemfusekit.df import DFSettings, DF, Table


class TestLLDF(unittest.TestCase):
    """Test suite for the LLDF module."""

    def test_file_loading(self):
        """Test case against file loading errors."""
        # load a non-existent file on purpose
        settings = DFSettings(
            output='none'
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
                output='none'
            )

            table1 = Table(
                file_path='tests/qepas.xlsx',
                sheet_name='Sheet1',
                preprocessing='qpl'
            )

            df = DF(settings, [table1])
            df.fuse()

        # Now a correct value:
        settings = DFSettings(output='none')
        table1 = Table(
            file_path='tests/qepas.xlsx',
            sheet_name='Sheet1',
            preprocessing='snv'
        )
        df = DF(settings, [table1])
        df.fuse()

    def test_export(self):
        """Test case against wrong export settings."""
        settings = DFSettings(output='none')
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

    def test_midlevel_data_fusion(self):
        """Integration test case for mid-level data fusion."""

        # PCA
        df_settings = DFSettings(output='graphical')
        table1 = Table(
            file_path='tests/qepas.xlsx',
            sheet_name='Sheet1',
            preprocessing='snv',
            feature_selection='pca'
        )
        table2 = Table(
            file_path='tests/rt.xlsx',
            sheet_name='Sheet1',
            preprocessing='none'
        )

        tables = [table1, table2]

        df = DF(df_settings, tables)
        df.fuse()

        # PLSDA
        df_settings = DFSettings(output='graphical')
        table1 = Table(
            file_path='tests/qepas.xlsx',
            sheet_name='Sheet1',
            preprocessing='snv',
            feature_selection='plsda'
        )
        table2 = Table(
            file_path='tests/rt.xlsx',
            sheet_name='Sheet1',
            preprocessing='none'
        )

        tables = [table1, table2]

        df = DF(df_settings, tables)
        df.fuse() 

    def test_matmul_datafusion(self):
        """Test case for outer product-based datafusion"""

        table1 = Table(
            file_path='tests/qepas.xlsx',
            sheet_name='Sheet1',
            preprocessing='snv',
            feature_selection='plsda'
        )
        table2 = Table(
            file_path='tests/rt.xlsx',
            sheet_name='Sheet1',
            preprocessing='none'
        )

        df = DF(DFSettings(method='outer'), [table1, table2])
        df.fuse()


if __name__ == '__main__':
    unittest.main()
