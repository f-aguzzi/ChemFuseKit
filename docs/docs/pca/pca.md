---
sidebar_position: 1
---

# PCA class

A class to store the data, methods and artifacts for _Principal Component Analysis_.

## Syntax

```python
PCA(settings: PCASettings, data: BaseDataModel)
```

## Constructor parameters

- `settings`: object of type [`PCASettings`](./pcasettings.md). Contains the settings for
  the `PCA` object.
- `data`: object of type [`BaseDataModel`](../base/basedatamodel.md). Contains the data to be analyzed.

## Fields

- `fused_data`: object of type [`LLDF`](../lldf/lldf-class.md). Contains the data to be analyzed.
- `components`: Number of components for the PCA analysis. Defaults to 0.
- `pca_model`: A `PCA` model from `scikit-learn`. Defaults to `None`.
- `settings`: object of type [`PCASettings`](./pcasettings.md). Contains the settings for
  the `PCA` object. 

## Methods

- `pca(self)`: performs Principal Component Analysis
- `pca_stats(self)`: produces PCA-related statistics and graphs.
- `export_data(self) -> PCADataModel`: exports a [`PCADataModel`](./pcadatamodel.md) with rescaled `array_scores` while maintaining the original `x_data`, `x_train` and `y` inherited by the constructor.
- `@classmethod from_file(cls, settings: PCASettings, model_path: str)`: creates a PCA instance from a file containing its sklearn core model.
  - *raises:*
    - `ImportError("The file you tried importing is not a valid Python object!")` when importing an invalid model;
    - `ImportError("The file you tried importing is not a sklearn PCA model!")` when the imported model is valid but an instance of the wrong class.

## Properties

- `rescaled_data(self) -> PCADataModel`: retrieves a [`PCADataModel`](./pcadatamodel.md) containing the results of PCA analysis (number of components, array scores, and dimension-reduced data).

<br />

## Example

```python
from chemfusekit.pca import PCA

# Initialize and run the PCA class
pca = PCA(lldf.fused_data, pca_settings)
pca.pca()

# Print the number of components and the statistics
print(pca.components)
pca.pca_stats()

# Get the rescaled data
rescaled_data = pca.rescaled_data
```