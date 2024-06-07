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

- `@classmethod def load_from_file(cls, import_path: str, sheet_name: str = 'Sheet1', class_column: str = 'Substance', index_column: str | None = None)`: creates an `LLDFDataModel` instance from an Excel file
- `export_to_file(export_path: str, sheet_name: str = 'Sheet1')`: exports the `LLDFDataModel` contents to an Excel table