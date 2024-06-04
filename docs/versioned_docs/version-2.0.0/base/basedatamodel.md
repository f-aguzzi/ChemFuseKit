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
