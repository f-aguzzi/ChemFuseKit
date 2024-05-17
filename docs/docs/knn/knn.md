---
sidebar_position: 1
---

# KNN class

A class to store the data, methods and artifacts for _k-Nearest Neighbors Analysis_.

## Syntax

```python
KNN(settings, fused_data)
```

## Constructor parameters

- `fused_data`: object of type [`LLDFModel`](../lldf/lldfmodel.md). Contains the data to be analyzed.
- `settings`: object of type [`KNNSettings`](knnsettings.md). Contains the settings for
  the `KNN` object.

The constructor can raise:
- `TypeError("Invalid settings: should be a KNNSettings-class object.")` if `settings` is of the wrong type
- `TypeError("Invalid fused_data: shold be a LLDFModel-class object.")` if `fused_data` is of the wrong type

## Fields

- `settings`: object of type [`KNNSettings`](/tesi/docs/knn/knnsettings). Contains the settings for
  the `KNN` object. 
- `fused_data`: onject of type ['LLDFModel`](/tesi/docs/lldf/lldfmodel). Contains the
  artifacts from the data fusion process.
- `model`: a `KNeighborsClassifier` model from `scikit-learn`. Defaults to `None`.

## Methods

- `knn(self)`: trains the k-Neighbors Analysis model
- `predict(self, x_data)`: performs LDA prediction once the model is trained.
  - *raises*:
    - `TypeError("X data for kNN prediction must be non-empty.")` if the input data is null
    - `RuntimeError("The kNN model is not trained yet!")` if the `KNN` model hasn't been trained yet

## Example

```python
from chemfusekit.knn import KNN

# Initialize and run the LDA class
knn = KNN(settings, lldf.fused_data)
knn.knn()

# Run predictions
knn.predict(x_data)
```