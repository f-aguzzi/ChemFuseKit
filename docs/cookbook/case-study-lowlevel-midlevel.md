---
sidebar_position: 5
---

# Case study: low-level vs mid-level data fusion

:::note
This case study is still **under construction**.

Even worse, it's comletely wrong. It's not only unfinished, it needs to be rewritten from scratch.
:::

## Introduction

## Methodology


---

```python
from chemfusekit.__base import BaseDataModel
from chemfusekit.lr import LRSettings, LR, GraphMode

# Let's import a raw table of QEPAS data
data = BaseDataModel.load_from_file(
    import_path='../tests/qepas.xlsx',
    sheet_name='Sheet1',
    class_column='Substance'
)

# Perform LR on the imported QEPAS data
lr_settings = LRSettings(output=GraphMode.GRAPHIC, test_split=True)
lr = LR(lr_settings, data)
lr.train()
```

The previous analysis (QEPAS-only) produced 4 misplaced samples, with a 97% overall accuracy.

Let's repeat it on GC data.

```python
# Let's import a raw table of QEPAS data
data = BaseDataModel.load_from_file(
    import_path='../tests/rt.xlsx',
    sheet_name='Sheet1',
    class_column='Substance'
)

# Perform LR on the imported QEPAS data
lr_settings = LRSettings(output=GraphMode.GRAPHIC, test_split=True)
lr = LR(lr_settings, data)
lr.train()
```

The GC-only analysis produced a 24.5% accurate model, which is an incredibly low score. Now let's try a low-level data fusion analysis.

```
from chemfusekit.df import DFSettings, DF, Table

# QEPAS table
table1 = Table(
    file_path='../tests/qepas.xlsx',
    sheet_name='Sheet1',
    class_column='Substance',
    preprocessing='snv'
)

# GC table
table2 = Table(
    file_path='../tests/rt.xlsx',
    sheet_name='Sheet1',
    class_column='Substance',
    preprocessing='none'
)

# Set up and perform data fusion
df = DF(DFSettings(), [table1, table1])
df.fuse()
data = df.fused_data

# Set up and perform LR
lr_settings = LRSettings(output=GraphMode.GRAPHIC, test_split=True)
lr = LR(lr_settings, data)
lr.train()
```

The results are completely undistinguishable from the QEPAS-only approach.

## Results

## Discussion

## Conclusion