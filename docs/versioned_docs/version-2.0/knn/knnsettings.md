---
sidebar-position: 1
---

# KNNSettings class

Holds the settings for the [`KNN`](knn.md) object.

Inherits from [`BaseSettings`](../base/basesettings.md).

## Syntax

```python
KNNSettings(
  n_neighbors: int,
  metric: str | Callable,
  weights: str | Callable,
  algorithm: str,
  output: GraphMode,
  test_split: false
)
```

## Fields and constructor parameters
- `n_neighbors`: the amount of components to be used in the `KNN` model. Defaults to 15.
- `metric`: the distance metric for the model. It can take one of the following values:
    - `minkwoski`
    - `precomputed`
    - `euclidean`
  or be a callable object.
- `weights`: the weight metric for the model. It can take one of the following values:
    - `uniform`
    - `distance`
  or be a callable object.
- `algorithm`: the algorithm for the model. It can take one of the following values:
    - `auto`
    - `ball_tree`
    - `kd_tree`
    - `brute`
  or be a callable object.
- `output`: toggles graph output mode. Defaults to [`GraphMode.NONE`](../utils/graphmode.md).
- `test_split`: toggles the training split test phase. Defaults to `False`. Requires `output` to be set to `True` to work.

The constructor raises:
- `ValueError("Invalid n_neighbors number: should be a positive integer.")` if the number of components is not valid.
- `ValueError("Invalid metric: should be 'minkwoski', 'precomputed', 'euclidean' or a callable.")` if the chosen metric is neither available nor a callable function.
- `ValueError("Invalid weight: should be 'uniform', 'distance' or a callable")` if the chosen weight is neither available nor a callable function.
- `ValueError("Invalid algorithm: should be 'auto', 'ball_tree', 'kd_tree' or 'brute'.")` if the chosen algotithm does not exist.
- `Warning("You selected test_split but it won't run because you disabled the output.")` if `test_split` is run with `output` set to false (split tests only produce graphical output, and are useless when run with disabled output).

## Example

```python
from chemfusekit.knn import KNNSettings, GraphMode

settings = KNNSettings(
    n_neighbors=20,     # pick 20 neighbors
    metric='minkowski', # choose the metric
    weights='distance', # choose the weight metric
    algorithm='auto',   # the best algorithm gets chosen automatically
    output=GraphMode.GRAPHIC, # graph output is enabled
    test_split=True # the model will be split-tested at the end of the training
)
```