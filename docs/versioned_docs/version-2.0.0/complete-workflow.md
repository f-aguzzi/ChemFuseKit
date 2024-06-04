---
sidebar-position: 7
---

# Complete workflow

Here's a sequence diagram to represent an example workflow, from the raw data
tables to classification, including data fusion, PCA and training.

```plantuml
actor User
participant LLDF
participant PCA
participant Classifier

User -> LLDF : Upload training tables
User -> LLDF : Set parameters
User -> Classifier : (optional) Upload model

LLDF -> PCA  : Pass preprocessed / fused tables
LLDF --> User  : Download fused tables
LLDF -> Classifier  : Pass preprocessed / fused tables \nRun classification
PCA -> Classifier : (optional) Set number of components

Classifier --> User : classification results, graphs
PCA --> User : classification results, graphs
Classifier --> User : (optional) download trained model

User -> Classifier : pass data to classify
Classifier --> User : classification results
```
