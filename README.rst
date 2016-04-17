pytest-cython
=============

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |appveyor| |requires|
        | |coveralls|
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

----

This `Pytest`_ plugin was generated with `Cookiecutter`_ along with
`@hackebrot`_'s `Cookiecutter-pytest-plugin`_ and `@ionelmc`_'s
`cookiecutter-pylibrary`_ templates.


Features
--------

* TODO


Requirements
------------

* TODO


Installation
------------

You can install "pytest-cython" via `pip`_ from `PyPI`_::

    $ pip install pytest-cython


Usage
-----

* TODO


Documentation
-------------

https://pytest-cython.readthedocs.org/


Contributing
------------
Contributions are very welcome. Tests can be run with `tox`_, please ensure
the coverage at least stays the same before you submit a pull request.

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


License
-------

* Free software: MIT license

Distributed under the terms of the `MIT`_ license, "pytest-cython" is free and
open source software


Issues
------

If you encounter any problems, please `file an issue`_ along with a detailed
description.


.. _`Cookiecutter`: https://github.com/audreyr/cookiecutter
.. _`@hackebrot`: https://github.com/hackebrot
.. _`@ionelmc`: https://github.com/ionelmc
.. _`MIT`: http://opensource.org/licenses/MIT
.. _`BSD-3`: http://opensource.org/licenses/BSD-3-Clause
.. _`GNU GPL v3.0`: http://www.gnu.org/licenses/gpl-3.0.txt
.. _`Apache Software License 2.0`: http://www.apache.org/licenses/LICENSE-2.0
.. _`cookiecutter-pytest-plugin`: https://github.com/pytest-dev/cookiecutter-pytest-plugin
.. _`cookiecutter-pylibrary`: https://github.com/ionelmc/cookiecutter-pylibrary
.. _`file an issue`: https://github.com/lgpage/pytest-cython/issues
.. _`pytest`: https://github.com/pytest-dev/pytest
.. _`tox`: https://tox.readthedocs.org/en/latest/
.. _`pip`: https://pypi.python.org/pypi/pip/
.. _`PyPI`: https://pypi.python.org/pypi
