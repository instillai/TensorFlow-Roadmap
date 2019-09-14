#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Use sphinx-quickstart to create your own conf.py file!
# After that, you have to edit a few things.  See below.

import sphinx_py3doc_enhanced_theme

# Select nbsphinx and, if needed, add a math extension (mathjax or pngmath):
extensions = [
    'nbsphinx',
    'sphinx.ext.mathjax',
]

# Exclude build directory and Jupyter backup files:
exclude_patterns = ['_build', '**.ipynb_checkpoints']

# Default language for syntax highlighting in reST and Markdown cells
highlight_language = 'none'

# Don't add .txt suffix to source files (available for Sphinx >= 1.5):
html_sourcelink_suffix = ''

# Execute notebooks before conversion: 'always', 'never', 'auto' (default)
#nbsphinx_execute = 'never'

# Use this kernel instead of the one stored in the notebook metadata:
#nbsphinx_kernel_name = 'python3'

# List of arguments to be passed to the kernel that executes the notebooks:
#nbsphinx_execute_arguments = ['--InlineBackend.figure_formats={"png", "pdf"}']

# If True, the build process is continued even if an exception occurs:
#nbsphinx_allow_errors = True

# Controls when a cell will time out (defaults to 30; use -1 for no timeout):
#nbsphinx_timeout = 60

# Default Pygments lexer for syntax highlighting in code cells:
#nbsphinx_codecell_lexer = 'ipython3'

# Width of input/output prompts used in CSS:
#nbsphinx_prompt_width = '8ex'

# If window is narrower than this, input/output prompts are on separate lines:
#nbsphinx_responsive_width = '700px'

# -- The settings below this line are not specific to nbsphinx ------------

master_doc = 'index'

project = 'TensorFlow-World-Resources'
author = 'Amirsina Torfi'
copyright = '2017, ' + author

linkcheck_ignore = [r'http://localhost:\d+/']

# -- Get version information from Git -------------------------------------

try:
    from subprocess import check_output
    release = check_output(['git', 'describe', '--tags', '--always'])
    release = release.decode().strip()
except Exception:
    release = '<unknown>'

# -- Options for HTML output ----------------------------------------------

html_title = project + ' version ' + release
html_theme = "sphinx_py3doc_enhanced_theme"
html_theme_path = [sphinx_py3doc_enhanced_theme.get_html_theme_path()]
html_logo = '_img/tflogo.gif'
html_theme_options = {
    'githuburl': 'https://github.com/astorfi/TensorFlow-World-Resources',
}

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    'papersize': 'a4paper',
    'preamble': r"""
\usepackage[sc,osf]{mathpazo}
\linespread{1.05}  % see http://www.tug.dk/FontCatalogue/urwpalladio/
\renewcommand{\sfdefault}{pplj}  % Palatino instead of sans serif
\IfFileExists{zlmtt.sty}{
    \usepackage[light,scaled=1.05]{zlmtt}  % light typewriter font from lmodern
}{
    \renewcommand{\ttdefault}{lmtt}  % typewriter font from lmodern
}
""",
}

latex_documents = [
    (master_doc, 'nbsphinx.tex', project, author, 'howto'),
]

latex_show_urls = 'footnote'




###########################################################################
#          auto-created readthedocs.org specific configuration            #
###########################################################################


#
# The following code was added during an automated build on readthedocs.org
# It is auto created and injected for every build. The result is based on the
# conf.py.tmpl file found in the readthedocs.org codebase:
# https://github.com/rtfd/readthedocs.org/blob/master/readthedocs/doc_builder/templates/doc_builder/conf.py.tmpl
#


import sys
import os.path
from six import string_types

from sphinx import version_info

# Get suffix for proper linking to GitHub
# This is deprecated in Sphinx 1.3+,
# as each page can have its own suffix
if globals().get('source_suffix', False):
    if isinstance(source_suffix, string_types):
        SUFFIX = source_suffix
    else:
        SUFFIX = source_suffix[0]
else:
    SUFFIX = '.rst'

# Add RTD Static Path. Add to the end because it overwrites previous files.
if not 'html_static_path' in globals():
    html_static_path = []
if os.path.exists('_static'):
    html_static_path.append('_static')
html_static_path.append('/home/docs/checkouts/readthedocs.org/readthedocs/templates/sphinx/_static')

# Add RTD Theme only if they aren't overriding it already
using_rtd_theme = False
if 'html_theme' in globals():
    if html_theme in ['default']:
        # Allow people to bail with a hack of having an html_style
        if not 'html_style' in globals():
            import sphinx_rtd_theme
            html_theme = 'sphinx_rtd_theme'
            html_style = None
            html_theme_options = {}
            if 'html_theme_path' in globals():
                html_theme_path.append(sphinx_rtd_theme.get_html_theme_path())
            else:
                html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

            using_rtd_theme = True
else:
    import sphinx_rtd_theme
    html_theme = 'sphinx_rtd_theme'
    html_style = None
    html_theme_options = {}
    if 'html_theme_path' in globals():
        html_theme_path.append(sphinx_rtd_theme.get_html_theme_path())
    else:
        html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
    using_rtd_theme = True

if globals().get('websupport2_base_url', False):
    websupport2_base_url = 'https://readthedocs.org/websupport'
    if 'http' not in settings.MEDIA_URL:
        websupport2_static_url = 'https://media.readthedocs.org/static/'
    else:
        websupport2_static_url = 'https://media.readthedocs.org//static'


#Add project information to the template context.
context = {
    'using_theme': using_rtd_theme,
    'html_theme': html_theme,
    'current_version': "py3doc-enh-theme",
    'MEDIA_URL': "https://media.readthedocs.org/",
    'PRODUCTION_DOMAIN': "readthedocs.org",
    'versions': [
    ("latest", "/en/latest/"),
    ("traditional-theme", "/en/traditional-theme/"),
    ("rtd-theme", "/en/rtd-theme/"),
    ("pyramid-theme", "/en/pyramid-theme/"),
    ("py3doc-enh-theme", "/en/py3doc-enh-theme/"),
    ("nature-theme", "/en/nature-theme/"),
    ("jupyter-theme", "/en/jupyter-theme/"),
    ("julia-theme", "/en/julia-theme/"),
    ("haiku-theme", "/en/haiku-theme/"),
    ("guzzle-theme", "/en/guzzle-theme/"),
    ("dotted-theme", "/en/dotted-theme/"),
    ("conda-again", "/en/conda-again/"),
    ("cloud-theme", "/en/cloud-theme/"),
    ("classic-theme", "/en/classic-theme/"),
    ("bootstrap-theme", "/en/bootstrap-theme/"),
    ("bizstyle-theme", "/en/bizstyle-theme/"),
    ("better-theme", "/en/better-theme/"),
    ("basicstrap-theme", "/en/basicstrap-theme/"),
    ("alabaster-theme", "/en/alabaster-theme/"),
    ("agogo-theme", "/en/agogo-theme/"),
    ],
    'downloads': [ 
    ("pdf", "//readthedocs.org/projects/nbsphinx/downloads/pdf/py3doc-enh-theme/"),
    ("htmlzip", "//readthedocs.org/projects/nbsphinx/downloads/htmlzip/py3doc-enh-theme/"),
    ],
    'subprojects': [ 
    ],
    'slug': 'nbsphinx',
    'name': u'nbsphinx',
    'rtd_language': u'en',
    'canonical_url': 'http://nbsphinx.readthedocs.io/en/0.2.14/',
    'analytics_code': '',
    'single_version': False,
    'conf_py_path': '/doc/',
    'api_host': 'https://readthedocs.org',
    'github_user': 'astorfi',
    'github_repo': 'TensorFlow-World-Resources',
    'github_version': 'py3doc-enh-theme',
    'display_github': True,
    'bitbucket_user': 'None',
    'bitbucket_repo': 'None',
    'bitbucket_version': 'py3doc-enh-theme',
    'display_bitbucket': False,
    'READTHEDOCS': True,
    'using_theme': (html_theme == "default"),
    'new_theme': (html_theme == "sphinx_rtd_theme"),
    'source_suffix': SUFFIX,
    'user_analytics_code': '',
    'global_analytics_code': 'UA-17997319-1',
    
    'commit': 'e949221b',
    
}
if 'html_context' in globals():
    html_context.update(context)
else:
    html_context = context

# Add custom RTD extension
if 'extensions' in globals():
    extensions.append("readthedocs_ext.readthedocs")
else:
    extensions = ["readthedocs_ext.readthedocs"]
