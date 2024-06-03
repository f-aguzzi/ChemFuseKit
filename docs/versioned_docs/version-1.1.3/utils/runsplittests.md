---
sidebar-position: 4
---

# `run_split_tests` function

A reusable function for split testing a generic model. Not meant for direct usage.

## Syntax

```python
run_split_test(x, y, model, extended=False, mode: GraphMode)
```

## Parameters

- `x` and `y`: the regressor and target arrays
- `model`: a `scikit-learn` classifier
- `extended`: a `bool` that selects whether a longer split analysis will be carried out
- `mode`: a [`GraphMode`](./graphmode.md) enum that acts as an output selector
