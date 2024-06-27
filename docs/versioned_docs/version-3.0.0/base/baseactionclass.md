---
sidebar_position: 1
---

# BaseActionClass class

A base abstract class from which all reducers and classifiers inherit.

## Syntax

```python
BaseActionClass(settings: BaseSettings, data: BaseDataModel)
```

## Constructor parameters

- `settings`: object of type [`BaseSettings`](./basesettings.md). Contains the settings for the `BaseActionClass` object.
- `data`: object of type [`BaseDataModel`](../base/basedatamodel.md). Contains the data to be analyzed.

## Fields

- `settings`: object of type [`BaseSettings`](./basesettings.md). Contains the settings for the `BaseActionClass` object.
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
