""" discover and run doctests in Cython extension modules."""
from _pytest.doctest import DoctestModule


def pytest_addoption(parser):
    group = parser.getgroup("cython")
    group.addoption(
        "--doctest-cython",
        action="store_true",
        default=False,
        help="run doctests in all .so and .pyd modules",
        dest="doctestcython",
        )
    group.addoption(
        "--cython-ignore-import-errors",
        action="store_true",
        default=True,
        help="ignore doctest ImportErrors",
        dest="doctest_ignore_import_errors",
        )


def _find_first_matching_path(path, extensions):
    for ext in extensions:
        newpath = path.new(ext=ext)
        if newpath.check():
            return newpath


def pytest_collect_file(path, parent):
    bin_exts = ['.so']
    cy_exts = ['.pyx', '.py']  # handle .so files if .py file exists
    config = parent.config

    if config.getvalue("--doctest-cython"):
        if path.ext in bin_exts:
            pyx_file = _find_first_matching_path(path, cy_exts)
            if pyx_file is not None:
                return DoctestModule(path, parent)
