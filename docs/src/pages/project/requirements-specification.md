---
title: Requirements Specification
author: Federico Aguzzi, Giorgio Felizzato
date: apr 18, 2024
---

# Requirements Specification

:::note
This requirements specification was written on April 18th, 2024. The project priorities have changed since then. For a constantly updated document about the philosophy and goals of this project, check out [Project Philosophy](./project-philosophy).
:::

## <u>Introduction</u>

The purpose of this project is twofold:

1. extract a library from [Dr
Felizzato](https://www.unibg.it/ugov/person/139887)'s chemometric classification
scripts;
2. create a GUI application on top of the extracted library to make it
  user-friendly.

To reuse as much code as possible from Felizzato's original scripts, the
project should be implemented in Python.

The project is partly inspired from the
[`Spectra`](https://www.spectrapp.unito.it/app/spectrapp) web app made by the
University of Torino, but with a twist: it will be based on an innovative _data
fusion_ approach that will analyze and process data from multiple sensors of
multiple types, all at once, to give the best possible chemometrical
classification on the given data.

## <u>Input data</u>

The chemometric data comes from two types of sensors: a gas chromatograph
and a gas spectrometer. The chromatograph outputs a single value for each
sample, a retention time in milliseconds. The spectrometer outputs an array of
spectrum responses for a set of infrared wavelength bands.

The data is stored in Excel files.

A dataset of pre-classified sample data from lab tests is available for the
purpose of training the classification algorithms.

### Pre-processing

The gas chromatography data requires rescaling. The spectrometry data can be
normalized, smoothed with a Savitski-Golay filter, or both.

## <u>Functionality</u>

### Data Analysis

The data can be analyzed with a PCA (Principal Component Analysis) pass to
assess whether its dimensionality can be reduced before the classification
process.

### Classification Algorithms

The available classification algorithms are:

- Logistic Regression
- Linear Discriminant Analysis
- Quadratic Discriminant Analysis
- Partial Least Squares Discriminant Analysis
- k-Nearest Neighbors
- Support Vector Machines

with extra options for each.

### User Interface

The application should have a graphical user interface similar to that of
_Spectra_, divided in steps and sections. In steps where multiple algorithms or
options are available, the choice will be made available through drop down
menus.

All outputs of all steps, including graphs, charts and elaborated data, will
need to be available for both previewing and saving at any time.

### Data Storage

For the algorithms that require training, an option to save and load trained
models is necessary. The models will be saved as files, locally, by the user.

### Integration

Given that intermiediate data can be loaded or saved at any point of the
process, the application will be interoperable with any kind of software that
can handle Excel tables.

### Security and Privacy

The application is meant to deal with forensic chemiometry, and the most
obvious implcation is that the processing of data must be rigorous.

As an additional requirement, if the application will be made web-based, it
must destroy all data stored remotely as soon as the session expires.

### Maintenance

This application, being born as an undergraduate thesis project, will not be
maintained by its original author. It is paramount, therefore, to make it as
maintainable, well-structured and well-documented as possible.

As an additional goal, it should be simple enough that non-programmers with a
Python background will be able to add new classification algorithms.

## <u>Extensions</u>

The first part of the project is the extraction of a library. The second is to
make a GUI app. Both will be extensible, but the _must-have_ goal is to make
the library in particular as usable (and reusable) as possible.

## <u>Required Documents</u>

Usage instructions must be provided.

Ample and extensive documentation on the source code, the project structure and
the chemometric algorithms used must be also provided, to aid future updates
and adjustments to the software.

## <u>Performance Requirements</u>

Since statistical training and classification are computation-heavy tasks, the
graphical components must be as light as possible, to avoid a further decrease
in the processing speed.

## <u>Feasibility</u>

Extracting the library is completely feasible. Making an application,
especially one that can be easily expanded and maintained, is a much more
complex task. In case the second will prove to be unachievable, a good enough
library will be acceptable on its own.
