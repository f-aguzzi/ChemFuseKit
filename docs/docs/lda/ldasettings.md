---
sidebar_position: 2
---

# LDASettings class

Holds the settings for the [`LDA`](./lda.md) object.

## Syntax

```python
LDASettings(components: int, output: GraphMode, split_test: bool)
```

## Fields and constructor parameters

- `components`: the amount of components to be used in the LDA model. Defaults to 3.
- `output`: toggles graph output. Defaults to [`GraphMode.NONE`](../utils/graphmode.md).
- `test_split`: toggles split testing. Defaults to `False`.


The constructor raises:
- `ValueError("Invalid component number: must be a > 1 integer.")` if the number of
  components is not valid.
- `Warning("You selected test_split but it won't run because you disabled the output.")` if split tests are run with `output` disabled

## Example

```python
from chemfusekit.lda import LDASettings, GraphMode

settings = LDASettings(
    components=(pca.components - 1),    # one less component than the number determined by PCA
    output=GraphMode.GRAPHIC, # graphs will be printed
    test_split=True # split testing is enabled
)
```