---
sidebar_position: 4
---

# Table class

Holds the information for a single table to import.

The [`LLDF`](./lldf-class.md) object takes a list of `Table` as a parameter.

## Syntax

```python
Table(
    file_path: str
    sheet_name: str
    preprocessing: str
    class_column: str
    index_column: str | None
)
```

## Fields and constructor parameters

- `file_path`: a `str` containing the path to the Excel datasheet
- `sheet_name`: a `str` containing the name of the sheet to select within the Excel file
- `preprocessing`: a `str` with the name of the preprocessing to be applied to the table.
   Available options: `snv` (normalization), `savgol` (Savitski-Golay smoothing), `savgol+snv` (both), `none` (no processing).
- 'class_column': a 'str' indicating the name of the class column within the Excel datasheet. Defaults to 'Substance'.
- 'index_column': a 'str' | `None` indicating the name of the index column within the Excel datasheet. Defaults to `None` (and in that case, the first column will be treated as the index).

## Example

```python
from chemfusekit.lldf import Table

# Create a table
table1 = Table(
    file_path='tests/qepas.xlsx',
    sheet_name='Sheet1',
    preprocessing='snv', # normalization preprocessing; other options: savgol, both or none
    class_column: 'substance',  # The column called 'substance' in the datase will be treated as the class column
    index_column: 'sample'  # The column named 'index' in the dataset will be treated as the index column 
)
```