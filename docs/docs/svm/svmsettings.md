---
sidebar_position: 2
---

# SVMSettings class

Holds the settings for the [`SVM`](./svm.md) object.

## Syntax

```python
SVMSettings(kernel, output)
```

## Fields and constructor parameters

- `kernel`: the type of kernel to use in the SVM analysis. Available options:
  - `linear`
  - `poly`
  - `gaussian`
  - `sigmoid`
  Defaults to `linear`.
- `output`: toggles graph output. Defaults to `False`.

The constructor raises:
- `TypeError("Kernel cannot be null.")` if the kernel type is null
- `ValueError("Invalid type: must be linear, poly, gaussian or sigmoid")` if the selected kernel is not one of the available
- `TypeError("Output selection cannot be null.")` if the output selection is invalid

## Example

```python
from chemfusekit.svm import SVMSettings

# Initialize the settings for Support Vector Machine
svm_settings = SVMSettings(
    type='linear',
    output=True # graphs will be printed
)
```