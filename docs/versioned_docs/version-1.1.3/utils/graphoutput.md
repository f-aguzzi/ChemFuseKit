---
sidebar-position: 2
---

# `graph_output` function

A (partially) reusable graphing function shared by different classes. Not meant for direct usage.

## Syntax

```python
graph_output(scores, model, name: str, mode: GraphMode)
```

## Parameters

- `scores`: the scores that are output by the model fitting function
- `model`: a `scikit-learn` classification model
- `name`: a `str` representing the name of the analysis technique
- `mode`: a [`GraphMode`](./graphmode.md) enum that acts as an output selector
