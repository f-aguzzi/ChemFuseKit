---
title: Project Philosophy
desc: A brief description of the ideas behind this project
---

# Project Philosophy

This is the core idea behind the project:

> A well-structured system, built upon existing open source components, enables non-programmers to edit and enhance it, solving practical issues while remaining easily expandable by direct users - a feat accomplished through software engineering contributions.

How do I (hope to) accomplish this?

- by setting up a sound template for new classes
- by setting up automated building and publishing tools that take away much of the burden of distributing a python project
- by making the simplest possible design choices

## Always available

One of the major decisions I took when planning the project was to follow the [eXtreme Programming](http://www.extremeprogramming.org) doctrine of daily builds: I wanted to always have a working version available even while adding new features. The project is semantically versioned and run through a CI/CD pipeline at each commit.
