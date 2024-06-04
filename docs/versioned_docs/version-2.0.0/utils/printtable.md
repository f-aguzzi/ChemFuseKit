---
sidebar-position: 3
---

# `print_table` function

A multimodal table printing utility. It can output tables as `Plotly` plots or as plain text. Not meant for direct usage.

## Syntax

```python
print_table(header_values, cell_values, title: str, mode: GraphMode)
```

## Parameters

- `header_values`: the column titles
- `cell_values`: a row array of column arrays
- `title`: a `str` containing the title for the table
- `mode`: a [`GraphMode`](./graphmode.md) enum that acts as an output selector