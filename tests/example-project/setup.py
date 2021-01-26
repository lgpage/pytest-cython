#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from __future__ import absolute_import


if __name__ == "__main__":
    import os
    import sys
    import glob

    from setuptools import setup
    from setuptools import Extension

    root = os.path.dirname(__file__)
    directives = {
        'profile': True,
        'embedsignature': True,
        'linetrace': False,
    }

    # Enable code coverage for C code: we can't use CFLAGS=-coverage in
    # tox.ini, since that may mess with compiling dependencies (e.g. numpy).
    # Therefore we set SETUPPY_CFLAGS=-coverage in tox.ini and copy it to
    # CFLAGS here (after deps have been safely installed).
    macros = []
    if 'TOXENV' in os.environ and 'SETUPPY_CFLAGS' in os.environ:
        os.environ['CFLAGS'] = os.environ['SETUPPY_CFLAGS']
        if '-coverage' in os.environ['SETUPPY_CFLAGS']:
            directives['linetrace'] = True
            macros = [[('CYTHON_TRACE', '1'), ('CYTHON_TRACE_NOGIL', '1')]]


    try:
        sys.argv.remove("--use-cython")
        use_cython = True
        from Cython.Build import cythonize
        from Cython.Distutils import build_ext
    except ValueError:
        use_cython = False
        from distutils.command.build_ext import build_ext

    if 'clean' in sys.argv:
        [os.remove(x) for x in glob.glob(os.path.join(root, 'src/pypackage/*.c'))]
        [os.remove(x) for x in glob.glob(os.path.join(root, 'src/pypackage/*.so'))]
        [os.remove(x) for x in glob.glob(os.path.join(root, 'src/pypackage/*.cpp'))]

    if use_cython:
        ext_files = glob.glob(os.path.join(root, 'src/pypackage/*.pyx'))
        ext_files.extend(glob.glob(os.path.join(root, 'src/pypackage/*.py')))
    else:
        ext_files = glob.glob(os.path.join(root, 'src/pypackage/*.c'))
        ext_files.extend(glob.glob(os.path.join(root, 'src/pypackage/*.cpp')))

    extensions = []
    exclude_files = ['__init__.py']
    include_dirs = [os.path.abspath(os.path.join(root, 'src/clib'))]
    for file_ in ext_files:
        basename = os.path.basename(file_)
        if basename in exclude_files:
            continue
        pyx_file, _ = os.path.splitext(basename)
        extensions.append(Extension(
                'src.pypackage.' + pyx_file,
                [file_],
                define_macros=macros,
                include_dirs=include_dirs,
            )
        )

    if use_cython:
        extensions = cythonize(
            extensions,
            force=True,
            compiler_directives=directives,
        )


    class optional_build_ext(build_ext):
        """Allow the building of C extensions to fail."""
        def run(self):
            try:
                build_ext.run(self)
            except Exception as e:
                self._unavailable(e)
                self.extensions = []  # avoid copying missing files (it would fail).

        def _unavailable(self, e):
            print('*' * 80)
            print('''WARNING:

        An optional code optimization (C extension) could not be compiled.

        Optimizations for this package will not be available!
            ''')

            print('CAUSE:')
            print('')
            print('    ' + repr(e))
            print('*' * 80)

    setup(
        name='pytest-cython',
        version='0.1.1',
        description="Example Cython project for pytest-cython tests",
        zip_safe=False,
        cmdclass={'build_ext': optional_build_ext},
        ext_modules=extensions,
    )
