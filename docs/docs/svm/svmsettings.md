---
sidebar_position: 2
---

# SVMSettings class

Holds the settings for the [`SVM`](./svm.md) object.

## Syntax

```python
SVMSettings(type=, output:
```

## Fields and constructor parameters

- `type`: the kernel to use in the SVM analysis. Available options:
  - `linear`
  - `poly`
  - `gaussian`
  - `sigmoid`
  Defaults to `linear`.
- `output`: toggles graph output. Defaults to `False`.

The constructor raises:
- `TypeError("Type cannot be null.")` if the kernel type is null
- `TypeError("Output selection cannot be null.")` if the output selection is invalid

## Example

```python
from svm import SVMSettings

# Initialize the settings for Support Vector Machine
svm_settings = SVMSettings(
    type='linear',
    output=True # graphs will be printed
)
```