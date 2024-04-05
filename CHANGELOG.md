# Changelog

## 0.2.2 Onwards

Please see the [GitHub releases](https://github.com/lgpage/pytest-cython/releases) for what has changed

## 0.2.1

The full list of merged changes is:

- #26: fix: pytest_collect_file to take into account pytest fspath deprecation in Node constructors
- #29: chore: use GitHub workflows in place of Travis
- #30: chore: use markdown project files
- #31: chore: add renovate bot

Special thanks to the following contributors that made this release possible:

- @AlenkaF
- @shvenkat

## 0.2.0

The full list of merged changes is:

- #11: Update tests
- #15, #17: Dropped support for Python 2, added support for Python 3.6+
- #18: New patched pyimport implementation, maintaining better compatibility with the installed pytest version
- #19: Rework how test collection works, making it possible to directly specify .pyx files to run, and reporting
    tests as being from the .pyx files as opposed to the compiled extension modules
- #20: Fix handling of cython generated autotestdicts; prevents running the same tests repeatedly, and adds better
    reporting of test line numbers
- #21: Add CI job with Windows
- #22: Various documentation improvements

Special thanks to the following contributors that made this release possible:

- @embray

## 0.1.1

The full list of merged changes is:

- #5: Fix DoctestModule deprecated error
- #6: Fix typo from #5
- #7: Fix support for relative imports
- #9: Maintain backwards compatibility for pytest 4.x

Special thanks to the following contributors that made this release possible:

- @embray
- @thrasibule

## 0.1.0

First release on PyPI (2016-04-17)
