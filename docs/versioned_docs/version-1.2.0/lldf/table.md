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
)
```

## Fields and constructor parameters

- `file_path`: a `str` containing the path to the Excel datasheet
- `sheet_name`: a `str` containing the name of the sheet to select within the Excel file
- `preprocessing`: a `str` with the name of the preprocessing to be applied to the table.
   Available options: `snv` (normalization), `savgol` (Savitski-Golay smoothing), `savgol+snv` (both), `none` (no processing).

## Example

```python
from chemfusekit.lldf import Table

# Create a table
table1 = Table(
    file_path='tests/qepas.xlsx',
    sheet_name='Sheet1',
    preprocessing='snv'  # normalization preprocessing; other options: savgol, both or none
)
```