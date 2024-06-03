---
sidebar_position: 1
---

# PLSDA class

A class to store the data, methods and artifacts for _Partial Least Squares Discriminant Analysis_.

## Syntax

```python
PLSDA(settings: PLSDASettings, fused_data: LLDFModel)
```

## Constructor parameters

- `settings`: object of type [`PLSDASettings`](plsdasettings.md). Contains the settings for
  the `PLSDA` object.
- `fused_data`: object of type [`LLDFModel`](../lldf/lldfmodel.md). Contains the data to be analyzed.

## Fields

- `settings`: object of type [`PLSDASettings`](./plsdasettings.md). Contains the settings for
  the `PLSDA` object. 
- `fused_data`: onject of type ['LLDFModel`](../lldf/lldfmodel.md). Contains the
  artifacts from the data fusion process.
- `model`: a `PLSRegression` model from `scikit-learn`. Defaults to `None`.

## Methods

- `plsda(self)`: trains the Partial Least Squares Discriminant Analysis model.
- `predict(self, x_data)`: performs PLSDA prediction once the model is trained.
  - *raises*:
    - `RuntimeError("The PLSDA model is not trained yet!")` if the `PLSDA` model hasn't been trained yet

## Example

```python
from chemfusekit.knn import PLSDA

# Initialize and run the LDA class
plsda = PLSDA(settings, lldf.fused_data)
plsda.plsda()

# Run predictions
plsda.predict(x_data)
```