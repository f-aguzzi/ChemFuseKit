---
sidebar_position: 1
---

# DF class

The `DF` class is used for _data fusion_ (low-level or mid-level).

## Syntax

```python
DF(df_settings: DFSettings, tables: List[Table])
```

## Constructor parameters

- `df_settings`: [`DFSettings`](./dfsettings)
  
  The settings for the LLDF object.

- `tables`: `List[`[`Table`](./table.md)`]`

  A list of `Table` objects containing info about the files to import

## Fields

- `settings`: [`DFSettings`](./dfsettings)
  
  The settings for the LLDF object.

- `tables`: `List[`[`Table`](./table.md)`]`

  A list of `Table` objects containing info about the files to import

- `fused_data`: [`DFModel`](./dfmodel.md) 

  The resulting model containing the data fusion artifacts.

## Methods

- `_snv(self, input_data)`: static method to rescale input arrays
- `fuse(self)`: performs data fusion on the data passed in the settings
  - *raises*:
    - `FileNotFoundError("Error opening the selected files.")`
      if the files specified in the settings are not valid
    - `SyntaxError("DF: this type of preprocessing does not exist")`
      if the preprocessing method specified in the settings is not valid
- `export_data(self, export_path)`: exports the data fusion artifacts to an Excel file
  - *raises*:
    - `RuntimeError("Cannot export data before data fusion.")` if export is
      attempted before fusing the data
    - `RuntimeError("Could not export data to the selected path.")` if any error
      happens during the export phase


## Example

```python
from chemfusekit.df import DF

# Initialize and run low-level data fusion
df = DF(tables, lldf_settings)
df.fuse()

# Export the LLDF data to an Excel file
df.export_data('output_file.xlsx')
```