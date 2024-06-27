---
sidebar-position: 7
---

# Complete workflow

Here's a sequence diagram to represent an example workflow, from the raw data
tables to classification, including data fusion, dimensionality reduction and training.

```plantuml
actor User
participant DF
participant Reducer
participant Classifier

User -> DF : Upload training tables
User -> DF : Set parameters
User -> Classifier : (optional) Upload model

DF -> Reducer  : Pass preprocessed / fused tables
DF --> User  : Download fused tables
DF -> Classifier  : Pass preprocessed / fused tables \nRun classification
Reducer -> Classifier : (optional) Set number of components

Classifier --> User : classification results, graphs
Reducer --> User : classification results, graphs
Classifier --> User : (optional) download trained model

User -> Classifier : pass data to classify
Classifier --> User : classification results
```
