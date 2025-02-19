---
sidebar_position: 1
---

# BaseClassifier class

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

- `settings`: object of type [`KNNSettings`](../knn/knnsettings). Contains the settings for
  the `BaseClassifier` object. 
- `data`: object of type [`BaseDataModel`](../base/basedatamodel.md). Contains the data to be analyzed.
- `model`: a `sklearn` model from `scikit-learn`. Defaults to `None`.

## Methods

- `import_model(import_path: str)`: loads a model from file
  - *raises*:
    - `ImportError("The file you tried importing is not a sklearn model!")`
- `export_model(export_path: str)`: exports a model to file
  - *raises*:
    - `RuntimeError("You haven't trained the model yet! You cannot export it now.")` when trying to export an untrained model
- `@classmethod from_file(cls, settings, model_path)`: creates a class instance by loading a model from file
  - *raises*:
    - `ImportError("The file you tried importing is not a sklearn model!")`
- `predict(x_data: pd.DataFrame)`: performs prediction through the `model`
  - *raises*:
    - `TypeError("X data for prediction must be non-empty.")` on empty `x_data`
    - `RuntimeError("The model is not trained yet!")` when run with an untrained `model`
