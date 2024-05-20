---
sidebar_position: 2
---

# LLDFSettings class

Holds the settings for the [`LLDF`](./lldf.md) object.

## Syntax

```python
LLDFSettings(
    qepas_path: str,
    qepas_sheet: str,
    rt_path:str,
    rt_sheet:str,
    preprocessing: str ='snv')
```

## Fields and constructor parameters

- `qepas_path`: a `str` containing the path to the QEPAS spectrography Excel datasheet
- `qepas_sheet`: a `str` containing the sheet name within the QEPAS Excel file
- `rt_path`: a `str` containing the path to the GC chromatrography Excel datasheet
- `rt_sheet`: a `str` containing the sheet name within the GC Excel file
- `preprocessing`: a `str` with the name of the preprocessing to be applied to the QEPAS data.
   Available options: `snv` (normalization), `savgol` (Savitski-Golay smoothing), `savgol+snv` (both).

The constructor throws:
- `TypeError("This type of preprocessing does not exist.")` if the preprocessing parameter is not one of the three available.

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