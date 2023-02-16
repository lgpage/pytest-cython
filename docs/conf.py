# -*- coding: utf-8 -*-
import os
import sys

import sphinx_py3doc_enhanced_theme

from pytest_cython import __version__ as release

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))


extensions = [
    'myst_parser',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.coverage',
    'sphinx.ext.doctest',
    'sphinx.ext.extlinks',
    'sphinx.ext.ifconfig',
    'sphinx.ext.napoleon',
    'sphinx.ext.todo',
    'sphinx.ext.viewcode',
]

if os.getenv('SPELLCHECK'):
    extensions += 'sphinxcontrib.spelling',
    spelling_show_suggestions = True
    spelling_lang = 'en_US'

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

master_doc = 'index'
project = 'pytest-cython'
year = '2021'
author = 'Logan Page'
copyright = '{0}, {1}'.format(year, author)

pygments_style = 'trac'
templates_path = ['.']
extlinks = {
    'issue': ('https://github.com/lgpage/pytest-cython/issues/%s', '#%s'),
    'pr': ('https://github.com/lgpage/pytest-cython/pull/%s', 'PR #%s'),
}

html_theme = "sphinx_py3doc_enhanced_theme"
html_theme_path = [sphinx_py3doc_enhanced_theme.get_html_theme_path()]
html_theme_options = {
    'githuburl': 'https://github.com/lgpage/pytest-cython/'
}

html_use_smartypants = True
html_last_updated_fmt = '%b %d, %Y'
html_split_index = True
html_sidebars = {
   '**': ['searchbox.html', 'localtoc.html', 'sourcelink.html'],
}

html_short_title = f'{project}-{release}'

napoleon_use_ivar = True
napoleon_use_rtype = False
napoleon_use_param = False
