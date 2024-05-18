---
sidebar_position: 2
---

# LRSettings class

Holds the settings for the [`LR`](./lr.md) object.

## Syntax

```python
LRSettings(algorithm: str, output: bool)
```

## Fields and constructor parameters

- `algorithm`: the amount of components to be used in the LDA model. Defaults to
  `liblinear`.  Other available options:
    - `lbfgs`
    - `newton-cg`
    - `newton-cholesky`
    - `sag`
    - `saga`
- `output`: toggles graph output. Defaults to `False`.

The constructor raises:
- `ValueError("This algorithm does not exist.")` if the selected `algorithm`
  is not a valid option.

## Example

```python
from chemfusekit.lr import LRSettings

settings = LRSettings(
    algorithm='newton-cg',
    output=True # graphs will be printed
)
```