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

- `settings`: object of type [`KNNSettings`](/tesi/docs/knn/knnsettings). Contains the settings for
  the `BaseClassifier` object. 
- `data`: object of type [`BaseDataModel`](../base/basedatamodel.md). Contains the data to be analyzed.
- `model`: a `sklearn` model from `scikit-learn`. Defaults to `None`.

## Methods

- `import_model(import_path: str)`: loads a model from file
- `export_model(export_path: str)`: exports a model to file
  - *raises*:
    - `RuntimeError("You haven't trained the model yet! You cannot export it now.")` when trying to export an untrained model
