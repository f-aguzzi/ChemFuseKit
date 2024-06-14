---
sidebar_position: 2
---

# 1. Project structure

In this cookbook page, you will be shown how the project is structured, and the purpose of each module.

## Project Hierarchy

```
chemfusekit
 │
 ├── base
 │    └── BaseDataModel
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

The entire library was streamlined to make operations as smooth and easy as possible. Any operation (import and export of both data and classifier models, training, processing, prediction, ...) looks the same on any class.

<br />

> *Want to update the settings in a classifier?*

You'll find the settings for `LDA` in `LDA.settings`. And the settings of `PCA` in `PCA.settings`. Where are the settings for `SVM`? In `SVM.settings`, of course. You get the hang of it.

<br />

> *Want to inspect the underlying `sklearn` model in one of the classifiers?

Let's say you're using a `LR` object. Its underlying sklearn classifier is in `LR.model`, as much as the underlying sklearn classifier of `KNN` is in `KNN.model`.

<br />

> *Want to swap out the data in a model and retrain it?*

Let's assume your new data is called `new_data`. Knowing that the training data, when present, is located in the `.data` field, just do this:

```python
knn.data = new_data
knn.train()
```

The training method is always called like its container class, but in lower case. To train a `KNN` model, like in this case, you just have to call `.knn()` on it. Same goes for `.lda()` on `LDA`, `.lldf()` on `LLDF`, and so on.


### Modular settings

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


### Modular classifiers

The classifiers themselves all inherit from a base class called [`BaseClassifier`](/docs/base/baseclassifier) in the `base` module:

```mermaid
classDiagram
    BaseDataModel <|-- DFDataModel
    BaseDataModel <|-- ReducerDataModel
    
    
    class BaseDataModel {
        x_data
        x_train
        y
        load_from_file()
        export_to_file()
    }

    class ReducerDataModel {
        n_components
    }

    class DFDataModel {
        tables
    }

    BaseActionClass <|.. BaseReducer
    BaseActionClass <|.. BaseClassifier

    BaseDataModel *-- BaseActionClass

    <<abstract>> BaseActionClass
    class BaseActionClass {
        train()
        settings
        data ~BaseDataModel~
        model
        from_file()
        import_model()
        export_model()
    }

    BaseReducer <|.. PCA
    BaseReducer <|.. LDA
    BaseReducer <|.. PLSDA

    <<abstract>> BaseReducer
    class BaseReducer {
        components
        rescaled_data
        export_data()
        reduce()
    }

    <<abstract>> BaseClassifier
    class BaseClassifier {
        predict()
    }

    BaseClassifier <| .. LDA
    BaseClassifier <| .. LR
    BaseClassifier <| .. SVM
    BaseClassifier <| .. KNN
    BaseClassifier <| .. PLSDA

    class PCA {
        pca_stats()
    }

    class LLDF {
        fuse_data()
    }

    class LR {
        array_scores
    }
```


### Modular data types

The data types are modular and interexchangeable too. Both [`LLDFDataModel`](/docs/lldf/lldfmodel) and [`PCADataModel`](/docs/pca/pcadatamodel) inherit from [`BaseDataModel`](/docs/base/basedatamodel) as shown in the following diagram:

```mermaid
classDiagram
    class BaseDataModel {
        +x_data: DataFrame
        +x_train: DataFrame
        +y: ndarray
        __init__(x_data, x_train, y)
    }

    class DFDataModel {
        ...
        __init__(...)
    }

    class ReducerDataModel {
        +components: int
        __init__(..., array_scores)
    }

    BaseDataModel *-- DFDataModel
    BaseDataModel *-- ReducerDataModel
```

This allows all the classifiers to use the `LLDF` data, dimension-reduced `PCA` data, or any other type of data as long as it follows the `BaseDataModel` template.


## File import and export

All the data models (`BaseDataModel`, and its derived, `LLDFDataModel` and `PCADataModel`) can export their content to Excel tables.

All classes derived from `BaseActionClass` (that is, all which derive from `BaseClassifier`, `BaseReducer`, or both) can import and export their sklearn data model from and to file.

All classifiers derived from `BaseClassifier` (`KNN`, `LDA`, `LR`, `PLSDA`, `SVM`) can perform training and inference.

All reducers derived from `BaseReducer` (`LDA`, `PCA`) can perform dimensionality reduction.