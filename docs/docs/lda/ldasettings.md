---
sidebar_position: 2
---

# LDASettings class

Holds the settings for the [`LDA`](./lda.md) object.

## Syntax

```python
LDASettings(components, output)
```

## Fields and constructor parameters

- `components`: the amount of components to be used in the LDA model. Defaults to 3.
- `output`: toggles graph output. Defaults to `False`.

The constructor raises:
- `ValueError("Invalid component number: must be a > 1 integer.")` if the number of
  components is not valid.

## Example

```python
from chemfusekit.lda import LDASettings

settings = LDASettings(
    components=(pca.components - 1),    # one less component than the number determined by PCA
    output=True # graphs will be printed
)
```