---
sidebar-position: 5
---

# `print_confuson_matrix` function

A multimodal confusion matrix and classification report printer utility. Not meant for direct usage.

## Syntax

```python
print_confusion_matrix(y1, y2, title: str, mode: GraphMode)
```

## Parameters

- `y1` and `y2`: the true and predicted values
- `title`: a `str` representing the title for the confusion matrix and classification report
- `mode`: a [`GraphMode`](./graphmode.md) enum that acts as an output selector