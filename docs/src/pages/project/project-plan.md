---
title: Project Plan
author: Federico Aguzzi
date: apr 18, 2024
---

# Project Plan

:::note
This project plan was written on April 18th, 2024. The project priorities have changed since then. For a constantly updated document about the philosophy and goals of this project, check out [Project Philosophy](./project-philosophy).
:::

A 14-point project plan, highlighting the strategies and techniques employed in
this project.

## 1. Introduction

This project is a small part of a larger initiative. [Professor Francesco
Saverio
Romolo](https://unibg.unifind.cineca.it/individual?uri=http%3A%2F%2Firises.unibg.it%2Fresource%2Fperson%2F80828)
and [Doctor Giorgio Felizzato](https://www.unibg.it/ugov/person/139887), two
chemists from the Law Department of our university, are conducting research on
the use of real-time gas-phase sensors for the purpose of forensics. This
initiative, too, is a subproject of the EU [_RISEN_](https://www.risen-h2020.eu)
project for real-time forensics. The sensors in use were developed for a
previous project Professor Romolo took part in, the
[_BONAS_](https://cordis.europa.eu/project/id/261685/reporting) project for
explosive precursor detection.

Michele Verdi, a previous undergraduate thesist worked, under the guidance of
Doctor Felizzato, on a _data fusion_ module to join and preprocess datasets
from two different types of sensors, with the purpose of enabling a unitary,
more accurate analysis of the sensor data. In the meanwhile, Doctor Felizzato
worked on chemometric classification scripts to be run on the output of the
data fusion model. The purpose of this project is twofold: firstly, to extract
an easier-to-use library from those scripts, and then, to build a graphical
application on top of the library, to make the work publicly accessible to
chemists and forensic analysts with no background in coding.
The project will continue as long as funding remains available, and other
undergraduates from the Computer Engineering course will continue contributing
after my (Federico Aguzzi's) work is done.

The entirety of the project will have to comply with the directives of the
Italian State Police, which will be the first direct user of the results of
Professor Romolo's project. As of today, no existing software provides an
entire pipeline for analyzing chemometric forensic data, while also including
a data fusion system, preprocessing, training, classification, plotting and
graphing. The closest option is the [_Spectra_](http://spectrapp.unito.it) web
app from University of Turin, but it lacks data fusion and has limitations on
import-export operations during intermediate phases.

Doctor Felizzato will take the role of the _product owner_, while [Professor
Angelo Michele Gargantini](https://cs.unibg.it/gargantini/) from the Department
of Management, Information and Production of the School of Engineering will
supervise the technical aspects of this project, to guarantee that computer
engineering principles are followed correctly. I (Federico Aguzzi) will be the
main developer and software engineer.

## 2. Process Model

The process model will take some key concepts from the [Agile
philosophy](https://agilemanifesto.org) while also maintaining a more rigorous
approach, as much as possible. Given that the core of the classification system
is already set out in Doctor Felizzato's scripts, and that I have no experience
with chemometrics, all the refactoring efforts will need to alter as little as
possible from the flow of data in the original code.

The development will be incremental: first will come the library, and then the
application. Classification techniques will be added one at a time. To ensure
that at least some part of the code will remain usable, the library needs to be
perfectly usable as a standalone, and to be compatible with [_Jupyter
Notebook_](https://jupyter.org).  As it was stated previously, other students
will continue the project, therefore it needs to be modularized and documented
well enough to allow other maintainers to build on it, especially the library,
in case the graphical application will ever need to be thrown out.

All requirements, use cases and class structures for the library will be
designed and represented through UML graphs before starting to code.

This project will also take some rules from the [_eXtreme
Programming_](http://www.extremeprogramming.org) playbook, mainly short or even
daily sprints, _test-driven development_ and _continuous integration_. This is
because the project development can be anticipated to be incredibly uneven and
hard to track; it is therefore paramount to make sure that an updated working
version of the software is always available, in case the development takes a
wrong turn at some point in the future.

The interface of the application will be designed with a mock-up prototype.
It's not the most efficient of techniques, but it's the only one that can
provide the degree of incrementality needed to integrate this part of the
project with the practices that will need to be used.

## 3. Project Organization

As stated in the introduction, the library and application that will result
from this project will be a small piece in a larger project by the Law
department, which, in turn, is also a smaller piece into the EU-wide Risen
project. The training data samples were provided by another university
participating in the project. The resulting software, in this or in an expanded
version, might be used experimentally by the State Police.

One major point is the need of interoperability of the data, which needs to be
available for export at any point during the processing, including datasets,
trained models and other pieces of information.

The data fusion module needs to be _sensor-agnostic_ in the sense that its
operations should be easily be expanded in case new types of sensors will be
used by the Risen project in the future.

## 4. Stadards, Guidelines, Procedures

The project will follow the [`PEP 8`](https://peps.python.org/pep-0008/)
formatting standard on all the `Python` code.

The SCM system will be [`git`](https://git-scm.com). All commits will follow the
[_Conventional Commits_](http://conventionalcommits.org) guidelines.

All graphs and diagrams will be made following the [`UML`](http://uml.org)
language standards.

All documents except the notes and devlogs in the
[`Obsidian`](https://obsidian.md) vault will be written in _Pandoc Markdown_
with \LaTeX extensions, and will be compiled to PDF with
[`pandoc`](https://pandoc.org). All the Obisidian notes will be written in plain
[Markdown](https://www.markdownguide.org) with the extensions provided by
Obisidian plugins.

Given that the development will be test-driven, testing will be carried out with
Python's built-in [`unittest`](https://docs.python.org/3/library/unittest.html)
module. The workflow will be made into a continuous integration via [`Github
Actions`](https://docs.github.com/en/actions).  At the end of each working day,
all the committed code will need to pass validation, automated tests and be
documented.

## 5. Management Activities

This project is mostly a single developer venture; however, given the size of
the task, self-management on my (Federico Aguzzi's) part is still required.
This will be made public through kanban boards within the Obsidian development
notes and through GitHub issues.

## 6. Risks

One possible risk is not to be able to finish the software within the time
frames imposed by my (Federico Aguzzi's) graduation. This risk will be
mitigated by front-lading the library extraction phase so that at least one
usable component will be produced by this project, and by implementing a
continuous integration, daily build approach that will ensure that a working
(albeit incomplete) version is available every day.

Another possible risk is making an application or library that produces
incorrect analyses from the provided data. To mitigate the risk, the
application will be tested against the original scripts from Dr Felizzato, and
thorough testing will be carried out.

## 7. Staff

Professor Romolo will be the client, with Dr Felizzato as the product owner.
Professor Gargantini will have a supervising role, while I (Federico Aguzzi)
will be the main developer for this subproject.

## 8. Methods and Techniques

Development will start from a requirements specification along with a
single-class proof-of-concept code prototype.

The user interface for the graphical application will be designed as an
evolutionary prototype, and then incrementally connected to the underlying
chemometrics library until all functionality is completely implemented.

All requirements, use cases and class structures for the library will be
designed and represented through UML graphs before starting to code.

The code will be tested at each commit through a continuous integration system
on the remote repository.


## 9. Quality Guarantees

Quality will follow from sound coding standards, thorough planning, rigorous
validation and testing, and high-coverage testing. No other measures will be
taken to improve quality, which should instead come as a _built-in_ factor if
all the previously listed principles are correctly followed.

The Python code within the project will be rejected via continuous integration
on the remote repository if it scores lower than 8/10 on Pylint quality tests.

## 10. Work Packages

The first and most important work package is the extraction of the library from
Dr Felizzato's scripts. All the following steps rely on the success of this
one. The work can be split in a planning phase (mainly UML diagram making) and
a coding phase (the actual refactor of the scripts to turn them into a library,
following the model).

The second work package is the creation of the web app. The work can be split
into two main avenues, a back end a and a front end. Both will require a
planning phase and a coding phase.

Both the library and the application will require extensive validation unit
testing, during and after the coding phase.


## 11. Resources

I (Federico Aguzzi) will be the main developer for this project, building on
the code previously written by Dr Felizzato and Michele Verdi. 

## 12. Budget and Schedule

This project has no budget.

A minimum viable version is projected to be available within the first half of
May. A fully implemented version is expected for mid-June.

## 13. Changes

The favored idea for the graphical application is to implement it as a web app.
In case it proves to be too difficult, too slow, or too hard to maintain, the
project will fall back onto a simpler desktop application.

## 14. Release

The software will be released incrementally. The repository will be shared with
the product owner. Following the philosophy of daily builds, a minimum viable
version will be available as soon as possible, and then it will be improved and
refined with each reiteration.
