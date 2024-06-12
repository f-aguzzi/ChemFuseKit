---
sidebar_position: 3
---

# BaseReducer class

A parent class for all reducers (decomposition-performing classes), containing basic shared utilities.
Inherits from [`BaseActionClass`](./baseactionclass.md).

## Syntax

```python
BaseReducer(settings: BaseSettings, data: BaseDataModel)
```
## Constructor parameters

- `settings`: object of type [`BaseSettings`](./basesettings.md). Contains the settings for the `BaseReducer` object.
- `data`: object of type [`BaseDataModel`](../base/basedatamodel.md). Contains the data to be analyzed.

## Fields

- `settings`: contains the settings for the `BaseReducer` object.
- `data`: object of type [`BaseDataModel`](../base/basedatamodel.md). Contains the data to be analyzed.
- `model`: a `sklearn` model from `scikit-learn` or `None`. Defaults to `None`.
- `components`: integer. The number of components to be kept after dimensionality reduction. Defaults to `0`.
- `rescaled_data`: `pd.DataFrame` or `None`. The data after being rescaled. Defaults to `None`.

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
- `@abstractmethod export_data(self) -> BaseDataModel`: exports the data in the `BaseDataModel` format.
- `reduce(self) -> BaseDataModel`: reduces the dimensionality of the data.
	+ *raises*:
		- `RuntimeError("The model hasn't been trained yet! You cannot use it to reduce data dimensionality.")` when run with an untrained `model`.

