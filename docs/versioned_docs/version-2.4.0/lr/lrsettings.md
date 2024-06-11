---
sidebar_position: 2
---

# LRSettings class

Holds the settings for the [`LR`](./lr.md) object.

Inherits from [`BaseSettings`](../base/basesettings.md).

## Syntax

```python
LRSettings(algorithm: str, output: GraphMode, test_split: bool)
```

## Fields and constructor parameters

- `algorithm`: the amount of components to be used in the LDA model. Defaults to
  `liblinear`.  Other available options:
    - `lbfgs`
    - `newton-cg`
    - `newton-cholesky`
    - `sag`
    - `saga`
- `output`: toggles graph output. Defaults to [`GraphMode.NONE`](../utils/graphmode.md).
- `test_split`: toggles split testing. Defaults to `False`.

The constructor raises:
- `ValueError("This algorithm does not exist.")` if the selected `algorithm`
  is not a valid option.
- `Warning("You selected test_split but it won't run because you disabled the output.")` if split tests are run with `output` disabled

## Example

```python
from chemfusekit.lr import LRSettings, GraphMode

settings = LRSettings(
    algorithm='newton-cg',
    output=GraphMode.GRAPHIC,   # graphs will be printed
    test_split=True # split testing is enabled
)
```