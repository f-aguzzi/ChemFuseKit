---
sidebar_position: 2
---

# LLDFSettings class

Holds the settings for the [`DF`](./df-class.md) object.

## Syntax

```python
DFSettings(output: GraphMode)
```

## Fields and constructor parameters
- `output`: toggles graph output. Defaults to [`GraphMode.NONE`](../utils/graphmode.md).

## Example

```python
from chemfusekit.df import DFSettings

# Initialize the settings for low-level data fusion
df_settings = DFSettings(output=GraphMode.TEXT)
```