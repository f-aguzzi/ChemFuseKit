---
sidebar_position: 1
---

# KNN class

A base class from which all classifiers inherit.

## Syntax

```python
BaseClassifier(settings: BaseSettings, data: BaseDataModel)
```

## Constructor parameters

- `settings`: object of type [`BaseSettings`](./basesettings.md). Contains the settings for
  the `BaseClassifier` object.
- `data`: object of type [`BaseDataModel`](../base/basedatamodel.md). Contains the data to be analyzed.

## Fields

- `settings`: object of type [`KNNSettings`](/tesi/docs/knn/knnsettings). Contains the settings for
  the `KNN` object. 
- `data`: object of type [`BaseDataModel`](../base/basedatamodel.md). Contains the data to be analyzed.
- `model`: a `sklearn` model from `scikit-learn`. Defaults to `None`.

## Methods

- `knn(self)`: trains the k-Neighbors Analysis model
- `predict(self, x_data)`: performs LDA prediction once the model is trained.
  - *raises*:
    - `RuntimeError("The kNN model is not trained yet!")` if the `KNN` model hasn't been trained yet
