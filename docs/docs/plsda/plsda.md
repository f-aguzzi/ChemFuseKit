---
sidebar_position: 1
---

# PLSDA class

A class to store the data, methods and artifacts for _Partial Least Squares Discriminant Analysis_.

It inherits from [`BaseClassifier`](../base/baseclassifier.md) and [`BaseReducer`](../base/basereducer.md), therefore it can perform both classification and feature selection.

## Syntax

```python
PLSDA(settings: PLSDASettings, data: BaseDataModel)
```

## Constructor parameters

- `settings`: object of type [`PLSDASettings`](plsdasettings.md). Contains the settings for
  the `PLSDA` object.
- `data`: object of type [`BaseDataModel`](../base/basedatamodel.md). Contains the data to be analyzed.

## Fields

- `settings`: object of type [`PLSDASettings`](./plsdasettings.md). Contains the settings for
  the `PLSDA` object. 
- `data`: object of type [`BaseDataModel`](../base/basedatamodel.md). Contains the data to be analyzed.
- `model`: a `PLSRegression` model from `scikit-learn`. Defaults to `None`.

## Methods

- `train(self)`: trains the Partial Least Squares Discriminant Analysis model.
- `predict(self, x_data)`: performs PLSDA prediction once the model is trained.
  - *raises*:
    - `RuntimeError("The PLSDA model is not trained yet!")` if the `PLSDA` model hasn't been trained yet
- `import_model(import_path: str)`: loads a model from file
	+ *raises*:
		- `ImportError("The file you tried importing is not a sklearn model!")`
- `export_model(export_path: str)`: exports a model to file
	+ *raises*:
		- `RuntimeError("You haven't trained the model yet! You cannot export it now.")` when trying to export an untrained model
- `@classmethod from_file(cls, settings, model_path)`: creates a class instance by loading a model from file
	+ *raises*:
		- `ImportError("The file you tried importing is not a sklearn model!")`
	+ *note*: this method creates an empty `BaseDataModel` object and assigns it to the `data` field of the class instance.
- `export_data(self) -> BaseDataModel`: exports the data in the `BaseDataModel` format.
- `reduce(self) -> BaseDataModel`: reduces the dimensionality of the data.
	+ *raises*:
		- `RuntimeError("The model hasn't been trained yet! You cannot use it to reduce data dimensionality.")` when run with an untrained `model`.
- `_select_feature_number(x, y)`: auto-selects the number of features using 5-fold cross-validation

## Example

```python
from chemfusekit.knn import PLSDA

# Initialize and run the LDA class
plsda = PLSDA(settings, lldf.fused_data)
plsda.train()

# Run predictions
plsda.predict(x_data)
```