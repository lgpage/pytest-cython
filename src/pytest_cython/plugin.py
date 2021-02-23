""" discover and run doctests in Cython extension modules."""

import pathlib
import sys
import sysconfig

import pytest
import py.path

import _pytest
from _pytest.doctest import get_optionflags
from _pytest.doctest import DoctestItem

try:
    from _pytest.pathlib import import_path  # pytest>=6.0 only
except ImportError:
    import_path = None

try:
    from _pytest.doctest import _get_checker
except ImportError:
    _get_checker = None


EXT_SUFFIX = sysconfig.get_config_var("EXT_SUFFIX")


def pytest_addoption(parser):
    group = parser.getgroup("cython")
    group.addoption(
        "--doctest-cython",
        action="store_true",
        default=False,
        help="run doctests in all .so and .pyd modules",
        dest="doctest_cython",
        )
    group.addoption(
        "--cython-ignore-import-errors",
        action="store_true",
        default=False,
        help="ignore doctest ImportErrors",
        dest="doctest_ignore_import_errors",
        )


def _find_matching_pyx_file(path, extensions):
    for ext in extensions:
        newpath = path.new(ext=ext)
        if newpath.check():
            return newpath


def pytest_collect_file(path, parent):
    bin_exts = ['.so']
    cy_exts = ['.pyx', '.py']  # collect .so files if .py file exists

    config = parent.config
    if path.ext in bin_exts:
        if config.getoption('--doctest-cython'):
            basename = path.basename.replace(EXT_SUFFIX, "")
            bin_file = path.new(purebasename=basename, ext=path.ext)

            pyx_file = _find_matching_pyx_file(bin_file, cy_exts)
            # only run test if matching .so and .pyx files exist
            # create addoption for this ??
            if pyx_file is not None:
                if hasattr(DoctestModule, 'from_parent'):
                    return DoctestModule.from_parent(parent, fspath=path)
                else:
                    # Backwards-compat for older pytest
                    return DoctestModule(path, parent)


class _PatchedLocalPath(py.path.local):
    """
    py.path.local path patched so that py.path.local.pyimport() will work
    if it is a PEP 3149 ABI extension module.  See _patch_pyimport.
    """

    @property
    def purebasename(self):
        return super().basename.replace(EXT_SUFFIX, '')

    def new(self, **kwargs):
        kwargs.pop('purebasename', None)
        return super().new(purebasename=self.purebasename, **kwargs)


class _PatchedPath(pathlib.Path):
    """
    Similar to _PatchedLocalPath but implements the equivalent hacks so that
    the `pathlib`-based ``import_path`` computes the module name correctly.
    """

    @property
    def stem(self):
        return super().name.replace(EXT_SUFFIX, '')

    def with_suffix(self, suffix):
        return self.with_name(self.stem + suffix)


# XXX patch pyimport to support PEP 3149
def _patch_pyimport(fspath, import_mode='prepend'):
    # pytest does not properly support PEP 3149 ABI tagged extension modules
    # (this should be fixed upstream); this provides an alternative
    # implementation (mostly copied from the original) which provides it

    # this supports pytest>=6.0 which uses import_path, as well as older
    # versions that use py.path.local.pyimport
    if isinstance(fspath, py.path.local):
        if fspath.basename.endswith(EXT_SUFFIX):
            fspath = _PatchedLocalPath(fspath)

        if import_mode == 'prepend':
            # the equivalent spelling in py.path.local.pyimport's
            # ensuresyspath argument
            import_mode = True

        return fspath.pyimport(ensuresyspath=import_mode)
    else:
        fspath = _PatchedPath(fspath)
        return import_path(fspath, import_mode=import_mode)


class DoctestModule(pytest.Module):

    def collect(self):
        import doctest

        if self.fspath.basename == "conftest.py":
            module = self.config.pluginmanager._importconftest(self.fspath)
        else:
            try:
                # XXX patch pyimport in pytest._pytest.doctest.DoctestModule
                module = _patch_pyimport(self.fspath)
            except ImportError:
                if self.config.getoption('--cython-ignore-import-errors'):
                    pytest.skip('unable to import module %r' % self.fspath)
                else:
                    raise

        # uses internal doctest module parsing mechanism
        finder = doctest.DocTestFinder()
        optionflags = get_optionflags(self)
        checker = None if _get_checker is None else _get_checker()
        runner = doctest.DebugRunner(verbose=0, optionflags=optionflags,
                                     checker=checker)
        for test in finder.find(module, module.__name__):
            if test.examples:  # skip empty doctests
                if hasattr(DoctestItem, 'from_parent'):
                    yield DoctestItem.from_parent(self, name=test.name,
                                                  runner=runner, dtest=test)
                else:
                    # Backwards-compat for older pytest
                    yield DoctestItem(test.name, self, runner, test)

    def _importtestmodule(self):
        # we assume we are only called once per module
        importmode = self.config.getoption("--import-mode", default="prepend")
        try:
            # XXX patch pyimport in pytest._pytest.pythod.Module
            mod = _patch_pyimport(self.fspath, importmode=importmode)
        except SyntaxError:
            raise self.CollectError(
                _pytest._code.ExceptionInfo().getrepr(style="short"))
        except self.fspath.ImportMismatchError:
            e = sys.exc_info()[1]
            raise self.CollectError(
                "import file mismatch:\n"
                "imported module %r has this __file__ attribute:\n"
                "  %s\n"
                "which is not the same as the test file we want to collect:\n"
                "  %s\n"
                "HINT: remove __pycache__ / .pyc files and/or use a "
                "unique basename for your test file modules"
                % e.args
            )
        # print "imported test module", mod
        self.config.pluginmanager.consider_module(mod)
        return mod
