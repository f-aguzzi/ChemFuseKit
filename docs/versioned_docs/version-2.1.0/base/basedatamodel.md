---
sidebar_position: 3
---

# BaseDataModel class

This class models the output data for all data-outputting operations (currently, the [`LLDF`](../lldf/lldf-class.md) operation and the [`PCA`](../pca/pca.md) operation).

## Syntax

```python
BaseDataModel(x_data: pd.DataFrame, x_train: pd.DataFrame, y: pd.DataFrame)
```

## Fields and constructor parameters

The first two are `Pandas` `DataFrame` objects:
- `x_data`
- `x_train`
The last is a `NumPy` `ndarray`:
- `y`

## Methods

Both methods are inherited from [`BaseDataModel`](../base/basedatamodel.md):

- `@classmethod def load_from_file(import_path: str, sheet_name: str = 'Sheet1')`: creates a `BaseDataModel` instance from an Excel file
- `export_to_file(export_path: str, sheet_name: str = 'Sheet1')`: exports the `BaseDataModel` contents to an Excel table
