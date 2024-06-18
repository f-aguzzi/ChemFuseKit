---
sidebar_position: 2
---

# LLDFSettings class

Holds the settings for the [`DF`](./df-class.md) object.

## Syntax

```python
DFSettings(output: GraphMode, method: str)
```

## Fields and constructor parameters
- `output`: toggles graph output. Defaults to [`GraphMode.NONE`](../utils/graphmode.md).
- `method`: a choice between `concat` (concatenation-based data fusion) and `outer` (outer matrix multiplication-based data fusion)

The constructor raises a `ValueError("DF: invalid method: must be 'concat' or 'outer'")` if an invalid parameter is provided to the `method` field.

## Example

```python
from chemfusekit.df import DFSettings

# Initialize the settings for low-level data fusion
df_settings = DFSettings(output=GraphMode.TEXT)
```