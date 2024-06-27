---
sidebar_position: 1
---

# LDA class

A class to store the data, methods and artifacts for _Linear Discriminant Analysis_.

It inherits from [`BaseClassifier`](../base/baseclassifier.md) and [`BaseReducer`](../base/basereducer.md), therefore it can perform both classification and feature selection.

## Syntax

```python
LDA(settings: LDASettings, data: BaseDataModel)
```

## Constructor parameters

- `settings`: object of type [`LDASettings`](./ldasettings.md). Contains the settings for
  the `LDA` object.
- `data`: object of type [`BaseDataModel`](../base/basedatamodel.md). Contains the data to be analyzed.

## Fields

- `settings`: object of type [`LDASettings`](./ldasettings.md). Contains the settings for
  the `LDA` object. 
- Fused data fields:
  - `x_data` 
  - `x_train`
  - `y`
- `model`: a `LinearDiscriminantAnalysis` model from `scikit-learn`. Defaults to `None`.

## Methods

- `train(self)`: performs Linear Discriminant Analysis
- `__print_prediction_graphs(self, y_test, y_pred)`: helper function to print
  graphs and stats about LDA predictions
- `predict(self, x_data)`: performs LDA prediction once the model is trained.
  - *raises*:
    - `RuntimeError("The LDA model is not trained yet!")` if the LDA model hasn't been trained yet
- `_select_feature_number(x, y)`: auto-selects the number of features using 5-fold cross-validation

## Example

```python
from chemfusekit.lda import LDA

# Initialize and run the LDA class
lda = LDA(lldf.fused_data, settings)
lda.train()
```