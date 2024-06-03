---
sidebar_position: 2
---

# LLDFSettings class

Holds the settings for the [`LLDF`](./lldf-class.md) object.

## Syntax

```python
LLDFSettings(output: GraphMode)
```

## Fields and constructor parameters
- `output`: toggles graph output. Defaults to [`GraphMode.NONE`](../utils/graphmode.md).

## Example

```python
from chemfusekit.lldf import LLDFSettings

# Initialize the settings for low-level data fusion
lldf_settings = LLDFSettings(output=GraphMode.TEXT)
```