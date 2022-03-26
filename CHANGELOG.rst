Changelog
=========

0.3.0
-----

The full list of merged PRs is:

* PR #15, #17: Dropped support for Python 2, added support for Python 3.6+
* PR #18: New patched pyimport implementation, maintaining better
  compatibility with the installed pytest version
* PR #19: Rework how test collection works, making it possible to directly
  specify .pyx files to run, and reporting tests as being from the .pyx
  files as opposed to the compiled extension modules
* PR #20: Fix handling of Cython-generated autotestdicts; prevents running
  the same tests repeatedly, and adds better reporting of test line numbers
* PR #21: Add CI job with Windows
* PR #22: Various documentation improvements


0.1.1
-----

The full list of merged PRs is:

* PR #5: Fix DoctestModule deprecated error
* PR #6: Fix typo from PR #5
* PR #7: Fix support for relative imports
* PR #9: Maintain backwards compatibility for pytest 4.x

Thanks to the following contributors who submitted PRs or reported issues that were merged/closed for this release:

- embray
- thrasibule


0.1.0
-----

First release on PyPI (2016-04-17).
