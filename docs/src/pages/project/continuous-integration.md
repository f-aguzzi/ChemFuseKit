---
title: Continuous Integration
description: Our continuous integration workflow.
---

# Continuous Integration

Our remote repository operates five continuous integration / continuous deployment workflows.

Two of the workflows are about code quality:
- a [`pylint`](https://pylint.readthedocs.io/en/stable/)` workflow that rejects commits with a code quality lower than 8.00
- a [`unittest`](https://docs.python.org/3/library/unittest.html) workflow that rejects commits that do not pass unit tests

A third workflow is about documentation deployment:
- a [`Docusaurus`](https://docusaurus.io) page builder that automatically deploys this documentation
  website to [`GitHub Pages`](https://pages.github.com)

A fourth workflow automates semantic releases.

A fifth, final workflow automates the building of the thesis document.