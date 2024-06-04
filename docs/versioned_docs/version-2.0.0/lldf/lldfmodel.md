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

