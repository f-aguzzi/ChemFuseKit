---
sidebar_position: 2
---

# Project structure

In this cookbook page, you will be shown how the project is structured, and the purpose of each module.

## Project Hierarchy

```
chemfusekit
 │
 ├── lda
 │    ├── LDASettings
 │    └── LDA
 │
 ├── lr
 │    ├── LRSettings
 │    └── LR
 │
 ├── plsda
 │    ├── PLSDASettings
 │    └── PLSDA
 │ 
 ├── pca
 │    ├── PCASettings
 │    ├── PCA
 │    └── PCADataModel
 │
 ├── lldf
 │    ├── LLDFSettings
 │    ├── LLDF
 │    └── LLDFDataModel
 │
 ├── svm
 │    ├── SVMSettings
 │    └── SVM
 │ 
 └── knn
      ├── KNNSettings
      └── KNN
```

As you can see, each module contains a class with the same name of the module, and a settings class. That's because this project tries to be as modular and as regular as possible, for clarity and interoperability.


## Modular design features

The settings for all classifiers (that is, all classes except `LLDF` and `PCA`) inherit from a base class called [`BaseSettings`](/docs/base/basesettings) in the `base` module:

```mermaid
classDiagram
    class BaseSettings {
        +output: GraphMode
        +test_split: bool
        __init__(output, test_split)
    }

    class KNNSettings {
        ...
    }

    class LDASettings {
        ...
    }

    class LRSettings {
        ...
    }

    class PLSDASettings {
        ...
    }

    class SVMSettings {
        ...
    }

    BaseSettings *-- KNNSettings
    BaseSettings *-- LDASettings
    BaseSettings *-- LRSettings
    BaseSettings *-- PLSDASettings
    BaseSettings *-- SVMSettings 
```

\
\
The classifiers themselves all inherit from a base class called [`BaseClassifier`](/docs/base/baseclassifier) in the `base` module:

```mermaid
classDiagram
    
    class BaseClassifier {
        +settings: BaseSettings
        +data: BaseDataModel
        +model: sklearn model
        __init__(settings, data)
        import_model(import_path: str)
        export_model(export_path: str)
        predict(x_data: pd.DataFrame)
    }

    class KNN {
        ...
    }

    class LDA {
        ...
    }

    class LR {
        ...
    }

    class PLSDA {
        ...
    }

    class SVM {
        ...
    }

    BaseClassifier *-- KNN
    BaseClassifier *-- LDA
    BaseClassifier *-- LR
    BaseClassifier *-- PLSDA
    BaseClassifier *-- SVM
```

\
\
The data types are modular and interexchangeable too. Both [`LLDFDataModel`](/docs/lldf/lldfmodel) and [`PCADataModel`](/docs/pca/pcadatamodel) inherit from [`BaseDataModel`](/docs/base/basedatamodel) as shown in the following diagram:

```mermaid
classDiagram
    class BaseDataModel {
        +x_data: DataFrame
        +x_train: DataFrame
        +y: ndarray
        __init__(x_data, x_train, y)
    }

    class LLDFDataModel {
        ...
        __init__(...)
    }

    class PCADataModel {
        +array_scores: ndarray
        +components: int
        __init__(..., array_scores)
    }

    BaseDataModel *-- LLDFDataModel
    BaseDataModel *-- PCADataModel
```

This allows all the classifiers to use the `LLDF` data, dimension-reduced `PCA` data, or any other type of data as long as it follows the `BaseDataModel` template.