---
title: Continuous Integration
description: Our continuous integration workflow.
---

# Continuous Integration

Our remote repository operates three continuous integration workflows.

Two of the workflows are about code quality:
- a `pylint` workflow that rejects commits with a code quality lower than 8.00
- a `unittest` workflow that rejects commits that do not pass unit tests

A third workflow is about documentation deployment:
- a `Docusaurus` page builder that automatically deploys this documentation
  website to `GitHub Pages`.