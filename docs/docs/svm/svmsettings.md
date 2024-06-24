---
sidebar_position: 2
---

# SVMSettings class

Holds the settings for the [`SVM`](./svm.md) object.

Inherits from [`BaseSettings`](../base/basesettings.md).

## Syntax

```python
SVMSettings(kernel: str, output: str, test_split: bool)
```

## Fields and constructor parameters

- `kernel`: the type of kernel to use in the SVM analysis. Available options:
  - `linear`
  - `poly`
  - `gaussian`
  - `sigmoid`
  Defaults to `linear`.
- `output`: toggles graph output. Defaults to [`none`] (other options: 'graphical', 'text'). Gets implicitly converted to a [`GraphMode` enum](../utils/graphmode.md).
- `test_split`: toggles split testing. Defaults to `False`.

The constructor raises:
- `ValueError("Invalid type: must be linear, poly, gaussian or sigmoid")` if the selected kernel is not one of the available
- `Warning("You selected test_split but it won't run because you disabled the output.")` if split tests are run with `output` disabled

## Example

```python
from chemfusekit.svm import SVMSettings

# Initialize the settings for Support Vector Machine
svm_settings = SVMSettings(
    type='linear',
    output='graphical',   # graphs will be printed
    test_split=True  # split testing is enabled
)
```