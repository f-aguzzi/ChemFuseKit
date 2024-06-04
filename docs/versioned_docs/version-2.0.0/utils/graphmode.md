---
sidebar-position: 1
---

# GraphMode enum

The `GraphMode` enum defines three possible values that the output of other classes can take:

- `GRAPHIC`: graphs, tables and stats will be rendered with `Plotly`, `MatPlotLib` or `Seaborn`. Best used with `Jupyter Notebook`;
- `TEXT`: output will be rendered as plain text. The best option for offline batch processing;
- `NONE`: output will be suppressed completely.