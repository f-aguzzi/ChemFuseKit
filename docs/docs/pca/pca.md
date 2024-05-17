---
sidebar_position: 1
---

# PCA class

A class to store the data, methods and artifacts for _Principal Component Analysis_.

## Syntax

```python
PCA(fused_data, settings)
```

## Constructor parameters

- `fused_data`: object of type [`LLDF`](../lldf/lldf.md). Contains the data to be analyzed.
- `settings`: object of type [`PCASettings`](./pcasettings.md). Contains the settings for
  the `PCA` object.

The constructor can raise:
- `TypeError("The LLDF model for PCA cannot be null.")` if `fused_data` is a null value
- `TypeError("The PCA settings object cannot be null.")` if `settings` is a null value

## Fields

- `fused_data`: object of type [`LLDF`](../lldf/lldf.md). Contains the data to be analyzed.
- `components`: Number of components for the PCA analysis. Defaults to 0.
- `pca_model`: A `PCA` model from `scikit-learn`. Defaults to `None`.
- `settings`: object of type [`PCASettings`](./pcasettings.md). Contains the settings for
  the `PCA` object. 

## Methods

- `pca(self)`: performs Principal Component Analysis
- `pca_stats(self)` produces PCA-related statistics and graphs.

## Example

```python
from chemfusekit.pca import PCA

# Initialize and run the PCA class
pca = PCA(lldf.fused_data, pca_settings)
pca.pca()

# Print the number of components and the statistics
print(pca.components)
pca.pca_stats()
```