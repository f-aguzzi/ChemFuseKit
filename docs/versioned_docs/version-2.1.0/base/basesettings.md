---
sidebar-position: 1
---

# BaseSettings class

Holds the settings for all classifier object. It's not meant for direct usage, only for inheritance.


## Syntax

```python
BaseSettings(output: GraphMode, test_split: false)
```

## Fields and constructor parameters
- `output`: toggles graph output mode. Defaults to [`GraphMode.NONE`](../utils/graphmode.md).
- `test_split`: toggles the training split test phase. Defaults to `False`. Requires `output` to be set to `True` to work.

The constructor raises:
- `Warning("You selected test_split but it won't run because you disabled the output.")` if `test_split` is run with `output` set to false (split tests only produce graphical output, and are useless when run with disabled output).
