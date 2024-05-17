---
sidebar_position: 2
---

# LLDFSettings class

Holds the settings for the [`LLDF`](./lldf.md) object.

## Syntax

```python
LLDFSettings(qepas_path, qepas_sheet, rt_path, rt_sheet, preprocessing='snv')
```

## Fields and constructor parameters

- `qepas_path`: a `string` containing the path to the QEPAS spectrography Excel datasheet
- `qepas_sheet`: a `string` containing the sheet name within the QEPAS Excel file
- `rt_path`: a `string` containing the path to the GC chromatrography Excel datasheet
- `rt_sheet`: a `string` containing the sheet name within the GC Excel file
- `preprocessing`: a `string` with the name of the preprocessing to be applied to the QEPAS data.
   Available options: `snv` (normalization), `savgol` (Savitski-Golay smoothing), `savgol+snv` (both).

## Example

```python
from chemfusekit.lldf import LLDFSettings

# Initialize the settings for low-level data fusion
lldf_settings = LLDFSettings(
    qepas_path='tests/qepas.xlsx',
    qepas_sheet='Sheet1',
    rt_path='tests/rt.xlsx',
    rt_sheet='Sheet1',
    preprocessing='snv'  # normalization preprocessing; other options: savgol or both
)
```