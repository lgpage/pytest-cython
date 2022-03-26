Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - |travis|
    * - package
      - |version| |downloads| |wheel| |supported-versions| |supported-implementations|

.. |docs| image:: https://readthedocs.org/projects/pytest-cython/badge/?style=flat
    :target: https://readthedocs.org/projects/pytest-cython
    :alt: Documentation Status

.. |travis| image:: https://api.travis-ci.org/lgpage/pytest-cython.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/lgpage/pytest-cython

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

This `Pytest`_ plugin allows for the doctesting of C extension modules
for Python, specifically created through `Cython`_.


Installation
============

You can install "pytest-cython" via `pip`_ from `PyPI`_::

    pip install pytest-cython


Usage
=====

Basic usage:

.. code-block:: shell

    pytest --doctest-cython

You can also run the doctests for a single ``.pyx`` file like:

.. code-block:: shell

    pytest --doctest-cython path/to/module.pyx

Note
----

* It is assumed that the C extension modules have been build inplace before
  running ``py.test`` and there is a matching Cython ``.pyx`` file


License
=======

* Free software: MIT license

Distributed under the terms of the `MIT`_ license, "pytest-cython" is free and
open source software


Issues
======

If you encounter any problems, please `file an issue`_ along with a detailed
description.


Acknowledgements
================

This `Pytest`_ plugin was generated with `Cookiecutter`_ along with
`@hackebrot`_'s `Cookiecutter-pytest-plugin`_ and `@ionelmc`_'s
`cookiecutter-pylibrary`_ templates.


.. _`Cookiecutter`: https://github.com/cookiecutter/cookiecutter
.. _`@hackebrot`: https://github.com/hackebrot
.. _`@ionelmc`: https://github.com/ionelmc
.. _`MIT`: https://opensource.org/licenses/MIT
.. _`cookiecutter-pytest-plugin`: https://github.com/pytest-dev/cookiecutter-pytest-plugin
.. _`cookiecutter-pylibrary`: https://github.com/ionelmc/cookiecutter-pylibrary
.. _`file an issue`: https://github.com/lgpage/pytest-cython/issues
.. _`pytest`: https://github.com/pytest-dev/pytest
.. _`tox`: https://tox.wiki/en/latest/
.. _`pip`: https://pypi.org/project/pip/
.. _`PyPI`: https://pypi.org
.. _`Cython`: https://cython.org/
