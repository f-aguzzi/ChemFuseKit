---
sidebar_position: 1
---

# LR class

A class to store the data, methods and artifacts for _Logistic Regression_.

## Syntax

```python
LR(settings, array_scores, y):
```

## Constructor parameters

- `settings`: object of type [`LRSettings`](./lrsettings.md). Contains the settings for
  the `LR` object.
- `array_scores`: product of [`PCA` analysis](../pca/).
- `y`: product of [`PCA` analysis](../pca/).

The constructor can raise:
- `TypeError("Settings cannot be null.")` if `settings` is a null value;
- `TypeError("Array scores cannot be null.")` if `array_scores` is a null value;
- `TypeError("Y cannot be null.")` if `y` is a null value.

## Fields

- `settings`: object of type [`LRSettings`](./lrsettings.md). Contains the settings for
  the `LR` object. 
- `array_scores`: product of [`PCA` analysis](../pca/).
- `y`: product of [`PCA` analysis](../pca/).
- `model`: A `LR` model from `scikit-learn`. Defaults to `None`.

## Methods

- `lr(self)`: performs Logistic Regression.
- `predict(self, x_sample)`: performs LR-based classification on input data.
    - *raises*:
        - `RuntimeError("The LR model is not trained yet!")` if prediction is
          started without training the model first;
        - `raise TypeError("X data for LDA prediction must be non-empty.")` if
          the data passed as argument is null.

## Example

```python
from chemfusekit.lr import LR

# Initialize and train the LR class
lr = LR(settings, array_scores, y)
lr.lr()

# Perform prediction
lr.predict(x_sample)
```