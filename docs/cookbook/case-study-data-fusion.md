---
sidebar_position: 4
---

# Case study: data fusion

:::note
This case study is still **under construction**.
:::


## Introduction

This case study aims to demonstrate the uniqueness of the data fusion - based workflow of ChemFuseKit for a unitary prediction and analysis. As a real-world example, a dataset containing data from three different sensors will be used to train a classifier able to distinguish between dimethyl methylphosphonate (DMMP) and acetone samples. The objective is to create a single, uninterrupted pipeline from the datasheets to the creation of the classifier and its export as a reusable model.


## Methodology

The complete pipeline, from data table to trained model, will go through the following steps:

```mermaid
stateDiagram-v2
    df: Data Fusion (LLDF)
    pca: Principal Component Analysis (PCA)
    
    state "Logistic Regression" as lr {
        st: Split test
        lrt: Logistic regression training
        fe: Model export

        [*] --> lrt
        lrt --> st : validate trained model
        st --> fe
        fe --> [*] : export model to file
    }

    [*] --> df : import tables
    df --> pca : pass fused dataset
    pca --> lr: pass dimension-reduced data
    lr --> [*]

    note right of df
    Available tables:
    - IMS
    - GC
    - QEPAS
    end note

    note left of pca
    Fused dataset received from LLDF:
    - x_data (fused tables)
    - y (class labels)
    - x_train (y + x_data)
    end note

    note left of lr
    Data received from PCA:
    - x_data (reduced dimensionality)
    - y (unchanged)
    - x_train (reduced dimensionality)
    - n_components (unused)
    - array_scores (reduced and rescaled PCA data)
    end note
```

### Data source

The data for this case study is sourced from the RISEN project. The data used in this study is presented in an Excel table containing information on 14 samples of DMMP (Dimethyl methylphosphonate) and 15 samples of acetone.

The Excel table contains three separate tables, each corresponding to a different type of sensor used to collect data on the chemical samples. The first table contains data collected using Ion Mobility Spectrometry (IMS), the second table contains data collected using Gas Chromatography (GC), and the third table contains data collected using Quartz-Enhanced Photo Acoustic Spectroscopy (QEPAS):

- IMS is a technique that separates and identifies ions based on their size and charge;
- GC is a widely used technique for separating and quantifying various chemical compounds in a sample;
- QEPAS is a more recent technique that uses the photoacoustic effect to detect and quantify trace amounts of gases.

Both spectrometers generate arrays of frequency responses that are focused around specific wavelengths, which are expressed in nanometers and serve as the column headers. In contrast, each chromatography sample contains a single value that signifies a retention time in milliseconds.


### Data preprocessing

The samples in the dataset need to be aligned and checked manually by the user, as requested by the RISEN specification. In this case, some DMMP samples in the IMS table were not correctly sorted by sample id, while the acetone samples recorded in the GC and QEPAS data did not match in all cases, so that only the intersection was kept.

The spectral data obtained from the IMS and QEPAS sensors are most effective when rescaled through normalization. This process ensures that the data is consistent and comparable across different samples. Additional data processing techniques, such as Savitski-Golay smoothing, may be employed to further reduce noise and filter out any outliers in the data. However, for the purpose of this case study, only normalization will be applied to the IMS and QEPAS data.

![IMS: original vs normalized](./img/IMS%20smoothing.png)

On the other hand, the GC data does not require any preprocessing. The data obtained from the GC sensor is already in a usable format and can be directly integrated with the data from the other sensors.

The most significant aspect of data preprocessing in this case study is data fusion. The three tables contained in the Excel datasheet are concatenated row-wise to form a single table that contains the data from the IMS and QEPAS spectrometers, as well as the GC retention times.

```python
from chemfusekit.lldf import LLDFSettings, LLDF, GraphMode, Table

# Initialize the settings to produce graphical output for the operation
settings = LLDFSettings(output=GraphMode.GRAPHIC)

# Set up the import settings for the first table (IMS spectral data)
table1 = Table(
    file_path='IMS_GC_QEPAS.xlsx',
    sheet_name='IMS',
    preprocessing='snv',
    class_column='Class',
    index_column='Sample_id'
)

# Set up the import settings for the second table (GC chromatography data)
table2 = Table(
    file_path='IMS_GC_QEPAS.xlsx',
    sheet_name='GC',
    preprocessing='none',
    class_column='Class',
    index_column='Sample_id'
)

# Set up the import settings for the third table (QEPAS spectral data)
table3 = Table(
    file_path='IMS_GC_QEPAS.xlsx',
    sheet_name='QEPAS',
    preprocessing='snv',
    class_column='Class',
    index_column='Sample_id'
)

# Now, let's make an array of the two tables
tables = [table1, table2, table3]

# Let's pass the settings and the tables to the LLDF constructor
lldf = LLDF(settings, tables)

# Let's finally perform data fusion with the lldf() method!
lldf.lldf()
```

### Dimensionality reduction

The resulting fused dataset is characterized by a very high dimensionality (hundreds of components). Many of these components are highly collinear, due to the nature of the spectral data (the values represent responses in specific bands, and those bands overlap partially). We can attempt a reduction of dimensionality while retaining the most amount of usable information by running PCA on the dataset.

The resulting fused dataset is characterized by a very high dimensionality, with hundreds of components, many of which are highly collinear due to the partial overlap of the spectral data bands. To address this issue and retain the most amount of usable information, we can attempt a reduction of dimensionality by running Principal Component Analysis (PCA) on the dataset. PCA is a statistical technique used to simplify high-dimensional data by transforming the original data into a new set of variables called principal components, which are linear combinations of the original variables. The first principal component captures the direction of the largest variability in the data, the second principal component captures the remaining variability orthogonal to the first component, and so on. By retaining only the first few principal components, one can often capture most of the information in the original data with fewer variables, making it easier to visualize and analyze.

In our case, we will set the PCA analysis to automatically select the number of components required to explain 99% of the original variance in the data, with a maximum limit of 10 components. If the target variance can be achieved with fewer than 10 components, the PCA analysis will use that lower number. Otherwise, all 10 will be utilized. Tests will be run with a 95% confidence interval.

```python
from chemfusekit.pca import PCASettings, PCA, GraphMode

# Retrieve the fused data from the lldf object of the previous step
fused_data = lldf.fused_data

# Initialize the settings for PCA with graph output
pca_settings = PCASettings(
    target_variance=0.99,
    confidence_level=0.95,
    initial_components=10,
    output=GraphMode.GRAPHIC
)

# Initialize and run PCA on the fused dataset
pca = PCA(pca_settings, fused_data)
pca.pca()

# Run the tests and statistics
pca.pca_stats()
```

At the end of the process, we can export the data to a new variable by using the `export_data()` method, which outputs a `PCADataModel` - class object (inheriting from `BaseDataModel`, and additionally contains the number of PCA variables, and the `array_scores`).

```python
# Get the data
reduced_dataset = pca.export_data()
```


### Model training

To classify our data, we will utilize a LR (Logistic Regression) object. The LR class is designed to automatically recognize the type of data it is provided with. In the case of receiving a PCADataModel object, it will default to using the array_scores as its x regressor for the logistic regression model.

```python
from chemfusekit.lr import LRSettings, LR, GraphMode

# Initialize the settings to produce graph output and perform split testing
lr_settings = LRSettings(output=GraphMode.GRAPHIC, test_split=True)

# Initialize and train LR
lr = LR(lr_settings, reduced_dataset)
lr.lr()
```

### Model evaluation

The LR model was configured to perform split testing, with 70% of the data allocated for the training set and the remaining 30% for the evaluation set. Upon completion of the model training, the confusion matrix and classification report indicated promising results.

![](./img/evaluation%20set.png)
![](./img/evalutation%20set%20confmatrix.png)

### Model export

The `LR` model can be exported using the `export_model(export_path: str)` method, which is inherited from its parent class `BaseClassifier` due to `LR` being a classifier itself.

```python
lr.export_model("LR_DMMP_acetone_classifier.sklearn")
```

In the future, when we need to classify DMMP and acetone on a new dataset, we can simply import the new dataset, perform the necessary data fusion, reduce the dimensionality through PCA, import the pre-trained `LR` model, and use it to classify the data. This streamlined process allows for efficient and consistent classification of DMMP and acetone samples.

```python
from chemfusekit.lldf import LLDFSettings, LLDF, GraphMode, Table
from chemfusekit.pca import PCASettings, PCA
from chemfusekit.lr import LRSettings, LR

# Data fusion
lldf_settings = LLDFSettings(output=GraphMode.GRAPHIC)
table1 = Table(
    file_path='new_dataset.xlsx',
    sheet_name='IMS',
    preprocessing='snv',
    class_column='Class',
    index_column='Sample_id'
)
table2 = Table(
    file_path='new_dataset.xlsx',
    sheet_name='GC',
    preprocessing='none',
    class_column='Class',
    index_column='Sample_id'
)
table3 = Table(
    file_path='new_dataset.xlsx',
    sheet_name='QEPAS',
    preprocessing='snv',
    class_column='Class',
    index_column='Sample_id'
)
tables = [table1, table2, table3]
lldf = LLDF(lldf_settings, tables)
lldf.lldf()
fused_data = lldf.fused_data

# PCA
pca_settings = PCASettings()
pca = PCA.from_file(pca_settings, "DMMP_acetone_pca.sklearn")
reduced_data = pca.reduce(fused_data)

# LR
lr_settings = LRSettings(output=GraphMode.GRAPHIC)
lr = LR.from_file(lr_settings, "LR_DMMP_acetone_classifier.sklearn")
prediction = lr.predict(reduced_data)
print(prediction)
```

![Predicted results](./img/prediction.png)