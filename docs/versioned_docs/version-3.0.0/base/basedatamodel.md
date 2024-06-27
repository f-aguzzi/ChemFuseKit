---
sidebar_position: 4
---

# BaseDataModel class

This class models the output data for all data-outputting operations (currently, the [`DF`](../df/df-class.md), the [`LDA`](../lda/lda.md), [`PLSDA`](../plsda/plsda.md) and the [`PCA`](../pca/pca.md) operations).

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

- `@classmethod load_from_file(cls, import_path: str, sheet_name: str = 'Sheet1', class_column: str = 'Substance', index_column: str | None = None):`: creates a `BaseDataModel` instance from an Excel, CSV or JSON file
- `export_to_file(export_path: str, sheet_name: str = 'Sheet1')`: exports the `BaseDataModel` contents to an Excel, CSV or JSON table depending on the extension specified in `export_path`
