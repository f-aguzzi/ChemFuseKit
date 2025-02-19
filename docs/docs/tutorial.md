---
sidebar_position: 1
---

# Tutorial

Let's discover **Data Fusion**.

As a simple example, we will train an LDA model and use it for classification.

First of all, let's install the package:
```bash
pip install chemfusekit 
```

## First step: data fusion

We will load the `DFSettings` with the paths to some Excel datasheets, containing
respectively the data from a QEPAS spectrometer and a GC chromatographer.

We will pick normalization as the preprocessing technique for the data.

The `DF` class will take these settings and perform low-level data fusion on the
two Excel tables we picked.

```python
from chemfusekit.df import DFSettings, DF

# Initialize the settings for low-level data fusion
df_settings = DFSettings(
    qepas_path='tests/qepas.xlsx',
    qepas_sheet='Sheet1',
    rt_path='tests/rt.xlsx',
    rt_sheet='Sheet1',
    preprocessing='snv'  # normalization preprocessing; other options: savgol or both
)

# Initialize and run low-level data fusion
df = DF(df_settings)
df.train()
```

Optionally, we can export the fused data into a new, single Excel datasheet:

```python
# (optional) export the LLDF data to an Excel file
df.export_data('output_file.xlsx')
```

## Second step: PCA

A run of Principal Component Analysis (`PCA`) will help us pick the right number
of components for the subsequent `LDA` analysis step.

As in the previous case, we will set it up with the help of the `PCASettings` class.

```python
from chemfusekit.pca import PCASettings, PCA

# Initialize the settings for Principal Component Analysis
pca_settings = PCASettings(
    target_variance=0.99,  # the minimum acceptable level of cumulative explained covariance
    confidence_level=0.05,  # the desired level of confidence
    initial_components=10,  # the initial amount of components for the iterative analysis
    output='graphical'  # graphs will be printed
)

# Initialize and run the PCA class
pca = PCA(df.fused_data, pca_settings)
pca.train()

# Print the number of components and the statistics
print(pca.components)
pca.pca_stats()
```

## Third step: LDA training

In this step we will set up the `LDASettings` and then run the `LDA` analysis with one less
component than what we figured out from the `PCA` analysis of the previous step.

```python
from chemfusekit.lda import LDASettings, LDA

settings = LDASettings(
    components=(pca.components - 1),  # one less component than the number determined by PCA
    output='graphical',     # graphs will be printed
    test_split=True  # Split testing is enabled
)

# Initialize and run the LDA class
lda = LDA(df.fused_data, settings)
lda.train()
```

## Fourth step: prediction

We will pick a random sample from the dataset and see whether the trained `LDA` model
can identify it correctly.

```python
# Let's pick a random sample from the dataset and see if it gets recognized correctly:
x_data_sample = lldf.fused_data[119] #   should be DMMP

# Let's run the prediction:
predictions = lda.predict(x_data_sample)
print(predictions)
```