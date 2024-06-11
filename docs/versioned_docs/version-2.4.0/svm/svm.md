---
sidebar_position: 1
---

# SVM class

A class to store the data, methods and artifacts for _Support Vector Machine Analysis_.

## Syntax

```python
SVM(settings: SVMSettings, data: BaseDataModel)
```

## Constructor parameters

- `settings`: object of type [`SVMSettings`](./svmsettings.md). Contains the settings for
  the `SVM` object.
- `data`: object of type [`BaseDataModel`](../base/basedatamodel.md). Contains the data to be analyzed.

The constructor raises:
- `ValueError("Fused data input cannot be empty.")` if the input data is null
- `valueError("Settings cannot be empty.")` if the settings are null

## Fields

- `fused_data`: object of type [`LLDFModel`](../lldf/lldfmodel.md). Contains the data to be analyzed.
- `settings`: object of type [`SVMSettings`](./svmsettings.md). Contains the settings for
  the `PCA` object. 
- `pca_model`: an `SVM` model from `scikit-learn`. Defaults to `None`.

## Methods

- `svm(self)`: performs Support Vector Machine analysis.
  - *raises*:
    - `ValueError(SVM: this type of kernel does not exist.")` if the kernel type is invalid
- `predict(self, x_data)`: performs classification based on SVM
  - *raises*:
    - `RuntimeError("The model hasn't been trained yet!")` if the model is null

## Example

```python
from chemfusekit.svm import SVM

# Initialize and run the SVM class
svm = LDA(lldf.fused_data, settings)
svm.svm()
```