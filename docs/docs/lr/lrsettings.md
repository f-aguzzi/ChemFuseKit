---
sidebar_position: 2
---

# LRSettings class

Holds the settings for the [`LR`](./lr.md) object.

## Syntax

```python
LRSettings(algorithm, output)
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
- `TypeError("The algorithm cannot be null.")` if the `algorithm` parameter is a
  null value;
- `TypeError("The output selector cannot be null.")` if the `output` parameter
  is a null value;
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