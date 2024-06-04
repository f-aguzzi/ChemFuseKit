---
sidebar_position: 1
---

# LLDF class

The `LLDF` class is used for _low-level data fusion_.

## Syntax

```python
LLDF(tables: List[Table], lldf_settings: LLDFSettings)
```

## Constructor parameters

- `tables`: `List[`[`Table`](./table.md)`]`

  A list of `Table` objects containing info about the files to import

- `lldf_settings`: [`LLDFSettings`](./lldfsettings)
  
  The settings for the LLDF object.

## Fields

- `settings`: [`LLDFSettings`](./lldfsettings)
  
  The settings for the LLDF object.

- `tables`: `List[`[`Table`](./table.md)`]`

  A list of `Table` objects containing info about the files to import

- `fused_data`: [`LLDFModel`](./lldfmodel.md) 

  The resulting model containing the data fusion artifacts.

## Methods

- `_snv(self, input_data)`: static method to rescale input arrays
- `lldf(self)`: performs low-level data fusion on the data passed in the settings
  - *raises*:
    - `FileNotFoundError("Error opening the selected files.")`
      if the files specified in the settings are not valid
    - `SyntaxError("LLDF: this type of preprocessing does not exist")`
      if the preprocessing method specified in the settings is not valid
- `export_data(self, export_path)`: exports the data fusion artifacts to an Excel file
  - *raises*:
    - `RuntimeError("Cannot export data before data fusion.")` if export is
      attempted before fusing the data
    - `RuntimeError("Could not export data to the selected path.")` if any error
      happens during the export phase


## Example

```python
from chemfusekit.lldf import LLDF

# Initialize and run low-level data fusion
lldf = LLDF(tables, lldf_settings)
lldf.lldf()

# Export the LLDF data to an Excel file
lldf.export_data('output_file.xlsx')
```