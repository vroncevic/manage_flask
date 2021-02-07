# -*- coding: utf-8 -*-

import os
import sys

sys.path.insert(0, os.path.abspath('../..'))

project = u'manage_flask'
copyright = u'2020, Vladimir Roncevic <elektron.ronca@gmail.com>'
author = u'Vladimir Roncevic <elektron.ronca@gmail.com>'
version = u'v1.1.0'
release = u'https://github.com/vroncevic/manage_flask/releases/'
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.viewcode']
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
language = None
exclude_patterns = []
pygments_style = None
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
htmlhelp_basename = 'manage_flaskdoc'
latex_elements = {}
latex_documents = [(
    master_doc, 'manage_flask.tex', u'manage\\_flask Documentation',
    u'Vladimir Roncevic \\textless{}elektron.ronca@gmail.com\\textgreater{}',
    'manual'
)]
man_pages = [(
    master_doc, 'manage_flask', u'manage_flask Documentation', [author], 1
)]
texinfo_documents = [(
    master_doc, 'manage_flask', u'manage_flask Documentation',
    author, 'manage_flask', 'One line description of project.',
    'Miscellaneous'
)]
epub_title = project
epub_exclude_files = ['search.html']
