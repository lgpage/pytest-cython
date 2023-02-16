# Overview

[![PyPI Package latest release](https://img.shields.io/pypi/v/pytest-cython.svg?style=flat)](https://pypi.org/project/pytest-cython)
[![PyPI Package monthly downloads](https://img.shields.io/pypi/dm/pytest-cython.svg?style=flat)](https://pypi.org/project/pytest-cython)
[![PyPI Wheel](https://img.shields.io/pypi/wheel/pytest-cython.svg?style=flat)](https://pypi.org/project/pytest-cython)
[![Supported versions](https://img.shields.io/pypi/pyversions/pytest-cython.svg?style=flat)](https://pypi.org/project/pytest-cython)
[![Supported implementations](https://img.shields.io/pypi/implementation/pytest-cython.svg?style=flat)](https://pypi.org/project/pytest-cython)

[![CI Check Status](https://github.com/lgpage/pytest-cython/actions/workflows/python-check.yml/badge.svg?branch=main)](https://github.com/lgpage/pytest-cython/actions/workflows/python-check.yml?query=branch%3Amain)
[![CI Tests Status](https://github.com/lgpage/pytest-cython/actions/workflows/python-test.yml/badge.svg?branch=main)](https://github.com/lgpage/pytest-cython/actions/workflows/python-test.yml?query=branch%3Amain)
[![Documentation Status](https://readthedocs.org/projects/pytest-cython/badge/?style=flat)](https://readthedocs.org/projects/pytest-cython)

This [pytest](https://github.com/pytest-dev/pytest) plugin allows for the doctesting of C extension modules for
Python, specifically created through [cython](https://cython.org/).

## Installation

You can install "pytest-cython" via [pip](https://pypi.org/project/pip/) from [PyPI](https://pypi.org):

``` shell
pip install pytest-cython
```

## Usage

Basic usage:

``` shell
pytest --doctest-cython
```

You can also run the doctests for a single `.pyx` file as such:

``` shell
pytest --doctest-cython path/to/module.pyx
```

### Note

It is assumed that the C extension modules have been build in place before running `py.test` and there is a
matching Cython `.pyx` file

## Issues

If you encounter any problems, please [file an issue](https://github.com/lgpage/pytest-cython/issues) along with a
detailed description.

## Acknowledgements

This [pytest](https://github.com/pytest-dev/pytest) plugin was generated with
[cookiecutter](https://github.com/cookiecutter/cookiecutter) along with [\@hackebrot](https://github.com/hackebrot)'s
[cookiecutter-pytest-plugin](https://github.com/pytest-dev/cookiecutter-pytest-plugin) and
[\@ionelmc](https://github.com/ionelmc)'s [cookiecutter-pylibrary](https://github.com/ionelmc/cookiecutter-pylibrary)
templates.
