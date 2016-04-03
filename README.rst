========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |appveyor| |requires|
        | |coveralls|
        | |codeclimate|
    * - package
      - |version| |downloads| |wheel| |supported-versions| |supported-implementations|

.. |docs| image:: https://readthedocs.org/projects/pytest-cython/badge/?style=flat
    :target: https://readthedocs.org/projects/pytest-cython
    :alt: Documentation Status

.. |travis| image:: https://travis-ci.org/lgpage/pytest-cython.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/lgpage/pytest-cython

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/lgpage/pytest-cython?branch=master&svg=true
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/lgpage/pytest-cython

.. |requires| image:: https://requires.io/github/lgpage/pytest-cython/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/lgpage/pytest-cython/requirements/?branch=master

.. |coveralls| image:: https://coveralls.io/repos/lgpage/pytest-cython/badge.svg?branch=master&service=github
    :alt: Coverage Status
    :target: https://coveralls.io/r/lgpage/pytest-cython

.. |codeclimate| image:: https://codeclimate.com/github/lgpage/pytest-cython/badges/gpa.svg
   :target: https://codeclimate.com/github/lgpage/pytest-cython
   :alt: CodeClimate Quality Status

.. |version| image:: https://img.shields.io/pypi/v/pytest-cython.svg?style=flat
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/pytest-cython

.. |downloads| image:: https://img.shields.io/pypi/dm/pytest-cython.svg?style=flat
    :alt: PyPI Package monthly downloads
    :target: https://pypi.python.org/pypi/pytest-cython

.. |wheel| image:: https://img.shields.io/pypi/wheel/pytest-cython.svg?style=flat
    :alt: PyPI Wheel
    :target: https://pypi.python.org/pypi/pytest-cython

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/pytest-cython.svg?style=flat
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/pytest-cython

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/pytest-cython.svg?style=flat
    :alt: Supported implementations
    :target: https://pypi.python.org/pypi/pytest-cython


.. end-badges

A plugin for testing Cython extension modules

* Free software: BSD license

Installation
============

::

    pip install pytest-cython

Documentation
=============

https://pytest-cython.readthedocs.org/

Development
===========

To run the all tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
