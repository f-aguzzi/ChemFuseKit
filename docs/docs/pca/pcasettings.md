---
sidebar_position: 2
---

# PCASettings class

Holds the settings for the [`PCA`](./pca.md) object.

## Syntax

```python
PCASettings(
  target_variance: float,
  confidence_level: float,
  initial_components: int,
  output: GraphMode
)
```

## Fields and constructor parameters

- `target_variance`: the minimum cumulative explained variance to reach in the analysis.
  Defaults to 0.95.
- `confidence_level`: the confidence level for statistical tests. Defaults to 0.05.
- `initial_components`: the minimum amount of components to be used in the PCA model.
  Defaults to 10.
- `output`: toggles graph output. Defaults to [`GraphMode.NONE`](../utils/graphmode.md).

## Example

```python
from chemfusekit.pca import PCASettings, GraphMode

# Initialize the settings for Principal Component Analysis
pca_settings = PCASettings(
    target_variance=0.99,
    confidence_level=0.05,
    initial_components=10,
    output=GraphMode.GRAPHIC  # graphs will be printed
)
```