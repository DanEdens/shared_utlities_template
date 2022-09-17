# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Setup root --------------------------------------------------------------
import os
import sys

# import sphinx_pdj_theme

root = os.path.abspath('../..')
sys.path.insert(0, root)

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'MinimTestKit'
copyright = '2022, Dan Edens'
author = 'Dan Edens'
release = '0.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
        'sphinx.ext.autodoc',
        'sphinx.ext.intersphinx',
        'sphinx.ext.ifconfig',
        'sphinx.ext.viewcode',
        'sphinx.ext.githubpages',
        'sphinxcontrib.confluencebuilder'
        ]

latex_elements = {
        # The paper size ('letterpaper' or 'a4paper').
        'papersize':    'letterpaper',
        # The font size ('10pt', '11pt' or '12pt').
        'pointsize':    '10pt',
        # Additional stuff for the LaTeX preamble.
        'preamble':     '',
        # Latex figure (float) alignment
        'figure_align': 'htbp',
        }


templates_path = ['_templates']
exclude_patterns = ['build/*']

# Publish after build, defaults to False
confluence_publish = os.environ.get("confluence_server_url", False)

# Import enviroment settings
confluence_space_name = os.environ.get("confluence_server_name", "danedens")
confluence_server_url = os.environ.get("confluence_server_url", "localhost")
confluence_server_user = os.environ.get("confluence_server_user", 'danedens31@gmail.com')
confluence_server_pass = os.environ.get("confluence_server_pass", 'Not Set')

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_short_title = 'testkitdocs'
html_static_path = ['_static']
html_show_sourcelink = False
html_show_sphinx = False
html_show_copyright = False
