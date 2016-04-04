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
        "--doctest-ignore-import-errors",
        action="store_true",
        default=True,
        help="ignore doctest ImportErrors",
        dest="doctest_ignore_import_errors",
        )


def _binary_file_for(path):
    bin_extensions = ['.so', '.pyd']
    for ext in bin_extensions:
        bin_file = path.new(ext=ext)
        if bin_file.check():
            return bin_file
    return None


def pytest_collect_file(path, parent):
    config = parent.config
    # let py.test --doctest-modules handle .py files even if they have been
    # compiled with Cython
    if path.ext == ".pyx":
        if config.getoption("--doctest-cython"):
            bin_file = _binary_file_for(path)
            if bin_file is not None:
                return DoctestModule(bin_file, parent)
