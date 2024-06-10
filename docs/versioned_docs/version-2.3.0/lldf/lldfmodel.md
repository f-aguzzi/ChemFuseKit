---
sidebar_position: 3
---

# LLDFDataModel class

This class models the output data from the [`LLDF`](./lldf-class.md) operation.

It inherits from the [`BaseDataModel`](../base/basedatamodel.md).

## Syntax

```python
LLDFModel(x_data: pd.DataFrame, x_train: pd.DataFrame, y: np.ndarray)
```

## Fields and constructor parameters

The first two are `Pandas` `DataFrame` objects:
- `x_data`
- `x_train`

The last is a `NumPy` `ndarray`:
- `y`

## Methods

Both methods are inherited from [`BaseDataModel`](../base/basedatamodel.md):

- `@classmethod load_from_file(cls, import_path: str, sheet_name: str = 'Sheet1', class_column: str = 'Substance', index_column: str | None = None):`: creates a `BaseDataModel` instance from an Excel, CSV or JSON file
- `export_to_file(export_path: str, sheet_name: str = 'Sheet1')`: exports the `BaseDataModel` contents to an Excel, CSV or JSON table depending on the extension specified in `export_path`