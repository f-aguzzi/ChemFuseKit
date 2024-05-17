---
sidebar_position: 1
---

# PLSDA class

A class to store the data, methods and artifacts for _Partial Least Squares Discriminant Analysis_.

## Syntax

```python
PLSDA(settings, fused_data)
```

## Constructor parameters

- `settings`: object of type [`PLSDASettings`](plsdasettings.md). Contains the settings for
  the `PLSDA` object.
- `fused_data`: object of type [`LLDFModel`](../lldf/lldfmodel.md). Contains the data to be analyzed.

The constructor can raise:
- `TypeError("Invalid settings: should be a PLSDASettings-class object.")` if `settings` is of the wrong type;
- `TypeError("Invalid fused_data: shold be a LLDFModel-class object.")` if `fused_data` is of the wrong type.

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
    - `TypeError("X data for PLSDA prediction must be non-empty.")` if the input data is null
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