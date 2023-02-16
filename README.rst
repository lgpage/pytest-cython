Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - package
      - |version| |downloads| |wheel| |supported-versions| |supported-implementations|
    * - tests
      - |ci-lint| |ci-test|
    * - docs
      - |docs|

.. |docs| image:: https://readthedocs.org/projects/pytest-cython/badge/?style=flat
    :alt: Documentation Status
    :target: https://readthedocs.org/projects/pytest-cython

.. |ci-lint| image:: https://github.com/lgpage/pytest-cython/actions/workflows/python-check.yml/badge.svg?branch=main
    :alt: CI Lint Status
    :target: https://github.com/lgpage/pytest-cython/actions/workflows/python-check.yml?query=branch%3Amain

.. |ci-test| image:: https://github.com/lgpage/pytest-cython/actions/workflows/python-test.yml/badge.svg?branch=main
    :alt: CI Lint Status
    :target: https://github.com/lgpage/pytest-cython/actions/workflows/python-test.yml?query=branch%3Amain

.. |version| image:: https://img.shields.io/pypi/v/pytest-cython.svg?style=flat
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/pytest-cython

.. |downloads| image:: https://img.shields.io/pypi/dm/pytest-cython.svg?style=flat
    :alt: PyPI Package monthly downloads
    :target: https://pypi.org/project/pytest-cython

.. |wheel| image:: https://img.shields.io/pypi/wheel/pytest-cython.svg?style=flat
    :alt: PyPI Wheel
    :target: https://pypi.org/project/pytest-cython

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/pytest-cython.svg?style=flat
    :alt: Supported versions
    :target: https://pypi.org/project/pytest-cython

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/pytest-cython.svg?style=flat
    :alt: Supported implementations
    :target: https://pypi.org/project/pytest-cython

.. end-badges

This `pytest`_ plugin allows for the doctesting of C extension modules for Python, specifically created through
`cython`_.


Installation
============

You can install "pytest-cython" via `pip`_ from `PyPI`_::

    pip install pytest-cython


Usage
=====

Basic usage:

.. code-block:: shell

    pytest --doctest-cython

You can also run the doctests for a single ``.pyx`` file as such:

.. code-block:: shell

    pytest --doctest-cython path/to/module.pyx

Note
----

It is assumed that the C extension modules have been build in place before running ``py.test`` and there is a
matching Cython ``.pyx`` file


Issues
======

If you encounter any problems, please `file an issue`_ along with a detailed description.


Acknowledgements
================

This `pytest`_ plugin was generated with `cookiecutter`_ along with `@hackebrot`_'s `cookiecutter-pytest-plugin`_
and `@ionelmc`_'s `cookiecutter-pylibrary`_ templates.


.. _`@hackebrot`: https://github.com/hackebrot
.. _`@ionelmc`: https://github.com/ionelmc
.. _`cookiecutter-pylibrary`: https://github.com/ionelmc/cookiecutter-pylibrary
.. _`cookiecutter-pytest-plugin`: https://github.com/pytest-dev/cookiecutter-pytest-plugin
.. _`cookiecutter`: https://github.com/cookiecutter/cookiecutter
.. _`cython`: https://cython.org/
.. _`file an issue`: https://github.com/lgpage/pytest-cython/issues
.. _`pip`: https://pypi.org/project/pip/
.. _`PyPI`: https://pypi.org
.. _`pytest`: https://github.com/pytest-dev/pytest
