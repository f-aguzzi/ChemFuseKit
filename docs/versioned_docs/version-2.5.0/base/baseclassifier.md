---
sidebar_position: 2
---

# BaseClassifier class

A parent class for all classifiers, containing basic shared utilities. Inherits from [`BaseActionClass`](./baseactionclass.md).

## Syntax

```python
BaseClassifier(settings: BaseSettings, data: BaseDataModel)
```
## Constructor parameters

- `settings`: object of type [`BaseSettings`](./basesettings.md). Contains the settings for the `BaseClassifier` object.
- `data`: object of type [`BaseDataModel`](../base/basedatamodel.md). Contains the data to be analyzed.

## Fields

- `settings`: object of type [`BaseSettings`](./basesettings.md). Contains the settings for the `BaseClassifier` object.
- `data`: object of type [`BaseDataModel`](../base/basedatamodel.md). Contains the data to be analyzed.
- `model`: a `sklearn` model from `scikit-learn` or `None`. Defaults to `None`.

## Methods

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
- `predict(self, x_data: pd.DataFrame)`: performs prediction once the model is trained
	+ *raises*:
		- `TypeError(f"X data for {self.__class__.__name__} prediction must be non-empty.")` on empty `x_data`
		- `RuntimeError(f"The {self.__class__.__name__} model is not trained yet!")` when run with an untrained `model`
