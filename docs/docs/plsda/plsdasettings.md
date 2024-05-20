---
sidebar_position: 2
---

# PLSDASettings class

Holds the settings for the [`PLSDA`](./plsda.md) object.

## Syntax

```python
PLSDASettings(n_components: int, output: bool, test_split: bool)
```

## Fields and constructor parameters

- `n_components`: number of components for the PLSDA analysis. Defaults to 3.
- `output`: toggles graph output. Defaults to `False`.
- `test_split`: toggles the training split test phase. Defaults to `False`. Requires `output` to be set to `True` to work.

The constructor raises:
- `ValueError("Invalid n_components number: should be a positive integer.")` if the number of components is below 1.
- `Warning("You selected test_split but it won't run because you disabled the output.")` if `test_split` is run with `output` set to false (split tests only produce graphical output, and are useless when run with disabled output).

## Example

```python
from chemfusekit.plsda import PLSDASettings

# Initialize the settings for Partial Least Squares Discriminant Analysis
plsda_settings = PLSDASettings(
    components=5,
    output=True, # graphs will be printed
    test_split=False    # no split testing
)
```