---
sidebar_position: 2
---

# Project structure

In this cookbook page, you will be shown how the project is structured, and the purpose of each module.

## Project Hierarchy

```
chemfusekit
 |
 |＿lda
 |  |＿LDASettings
 |  |＿LDA
 |
 |＿lr
 |  |＿LRSettings
 |  |＿LR
 |
 |＿plsda
 |  |＿PLSDASettings
 |  |＿PLSDA
 | 
 |＿pca
 |  |＿PCASettings
 |  |＿PCA
 |
 |＿lldf
 |  |＿LLDFSettings
 |  |＿LLDF
 |  |＿LLDFModel
 |
 |＿svm
 |  |＿SVMSettings
 |  |＿SVM
 |
 |＿knn
    |＿KNNSettings
    |＿KNN
```

As you can see, each module contains a class with the same name of the module, and a settings class. That's because this project tries to be as modular and as regular as possible, for clarity and interoperability.