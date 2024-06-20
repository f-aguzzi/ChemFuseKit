---
sidebar_position: 2
---

# DFSettings class

Holds the settings for the [`DF`](./df-class.md) object.

## Syntax

```python
DFSettings(output: str, method: str)
```

## Fields and constructor parameters
- `output`: toggles graph output. Defaults to [`none`] (other options: 'graphical', 'text'). Gets implicitly converted to a [`GraphMode` enum](../utils/graphmode.md).
- `method`: a choice between `concat` (concatenation-based data fusion) and `outer` (outer matrix multiplication-based data fusion)

The constructor raises a `ValueError("DF: invalid method: must be 'concat' or 'outer'")` if an invalid parameter is provided to the `method` field.

## Example

```python
from chemfusekit.df import DFSettings

# Initialize the settings for low-level data fusion
df_settings = DFSettings(output='text')
```