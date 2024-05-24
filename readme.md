# `chemfusekit`: Data Fusion and Analysis in Colab

[![linting: pylint](https://img.shields.io/badge/linting-pylint-yellowgreen)](https://github.com/pylint-dev/pylint)
[![Pylint](https://github.com/f-aguzzi/tesi/actions/workflows/pylint.yml/badge.svg)](https://github.com/f-aguzzi/tesi/)
[![Unittest](https://github.com/f-aguzzi/tesi/actions/workflows/unittest.yml/badge.svg)](https://github.com/f-aguzzi/tesi/)
[![](https://img.shields.io/badge/Read_the_docs-GitHub_Pages-darkorange)](https://f-aguzzi.github.io/tesi/)
[![Try It In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/f-aguzzi/tesi/blob/main/examples/pca_lda_example_notebook.ipynb)
<p align="center">
  <img src="https://raw.githubusercontent.com/f-aguzzi/tesi/main/docs/static/img/logo.svg" alt="Library Logo" style="width: 20%;">
</p>

A minimal Python / Jupyter Notebook / Colab library for data fusion and
chemometrical analysis.

Developed as Federico Aguzzi's Computer Engineering undergraduate thesis
project, under the supervision of Software Engineering Professor
[Angelo Michele Gargantini](https://cs.unibg.it/gargantini/),
based on the scripts made by Dr
[Giorgio Felizzato](https://www.unibg.it/ugov/person/139887)
and the research of Professor
[Francesco Saverio Romolo](https://unibg.unifind.cineca.it/individual?uri=http%3A%2F%2Firises.unibg.it%2Fresource%2Fperson%2F80828)
of the Law Department of the University of Bergamo. Further info on the project
[here](https://f-aguzzi.github.io/tesi/project).

<br />

Get it on `pip`:
```bash
pip install chemfusekit
```

<br />

You can also try this demo:

[![Try It In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/f-aguzzi/tesi/blob/main/examples/pca_lda_notebook.ipynb)

and find instructions [here](https://f-aguzzi.github.io/tesi/docs/tutorial).

<br />

## Features

- **data fusion**: join data from different sensors to increase the quality and
  precision of your chemometrical analysis
- **model training**: train, save and load statistical models
- **data classification**: use your models to classify and predict

Here's a list of the currently available modules:
- **LLDF**: *Low-Level Data Fusion*
- **PCA**: *Principal Component Analysis*
- **LDA**: *Linear Discriminant Analysis* ([demo](https://colab.research.google.com/github/f-aguzzi/tesi/blob/main/examples/pca_lda_notebook.ipynb))
- **SVM**: *Support Vector Machine* ([demo](https://colab.research.google.com/github/f-aguzzi/tesi/blob/main/examples/svm_notebook.ipynb))
- **LR**: *Logistic Regression* ([demo](https://colab.research.google.com/github/f-aguzzi/tesi/blob/main/examples/pca_lr_notebook.ipynb))
- **KNN**: *k_Neighbors Analysis* ([demo](https://colab.research.google.com/github/f-aguzzi/tesi/blob/main/examples/knn_notebook.ipynb))
- **PLSDA**: *Partial Least Squres Discriminant Analysis* ([demo](https://colab.research.google.com/github/f-aguzzi/tesi/blob/main/examples/plsda_notebook.ipynb))
