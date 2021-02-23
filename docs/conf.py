# -*- coding: utf-8 -*-
import os
import sys


sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))


extensions = [
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

source_suffix = '.rst'
master_doc = 'index'
project = 'pytest-cython'
year = '2021'
author = 'Logan Page'
copyright = '{0}, {1}'.format(year, author)


from pytest_cython import __version__ as release

pygments_style = 'trac'
templates_path = ['.']
extlinks = {
    'issue': ('https://github.com/lgpage/pytest-cython/issues/%s', '#'),
    'pr': ('https://github.com/lgpage/pytest-cython/pull/%s', 'PR #'),
}
import sphinx_py3doc_enhanced_theme
html_theme = "sphinx_py3doc_enhanced_theme"
html_theme_path = [sphinx_py3doc_enhanced_theme.get_html_theme_path()]
html_theme_options = {
    'githuburl': 'https://github.com/lgpage/pytest-cython/'
}

html_use_smartypants = True
html_last_updated_fmt = '%b %d, %Y'
html_split_index = True
html_sidebars = {
   '**': ['searchbox.html', 'globaltoc.html', 'sourcelink.html'],
}
html_short_title = f'{project}-{release}'

napoleon_use_ivar = True
napoleon_use_rtype = False
napoleon_use_param = False
