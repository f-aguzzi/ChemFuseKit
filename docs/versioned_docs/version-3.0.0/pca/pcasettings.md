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
  output: str 
)
```

## Fields and constructor parameters

- `target_variance`: the minimum cumulative explained variance to reach in the analysis.
  Defaults to 0.95.
- `confidence_level`: the confidence level for statistical tests. Defaults to 0.05.
- `initial_components`: the minimum amount of components to be used in the PCA model.
  Defaults to 10.
- `output`: toggles graph output. Defaults to [`none`] (other options: 'graphical', 'text'). Gets implicitly converted to a [`GraphMode` enum](../utils/graphmode.md).

## Example

```python
from chemfusekit.pca import PCASettings

# Initialize the settings for Principal Component Analysis
pca_settings = PCASettings(
    target_variance=0.99,
    confidence_level=0.05,
    initial_components=10,
    output='graphical'  # graphs will be printed
)
```