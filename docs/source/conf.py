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

source_suffix = {'.rst': 'restructuredtext'}

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

# Import enviroment settings
confluence_space_key = os.environ.get("confluence_server_key", "danedens")
confluence_server_url = os.environ.get("confluence_server_url", "localhost")
confluence_server_user = os.environ.get("confluence_server_user",
                                        'danedens31@gmail.com')
confluence_server_pass = os.environ.get("confluence_server_pass", False)

if confluence_server_pass:
    # Publish after build, defaults to False, requires pass is set
    confluence_publish = os.environ.get("confluence_server_publish", False)
else:
    confluence_publish = False

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# extensions.append("sphinxjp.themes.basicstrap")
html_themes = (
        'sphinx_material', 'alabaster', 'sphinx_rtd_theme',
        'furo', 'sphinx_book_theme', 'pydata_sphinx_theme',
        'press', 'piccolo_theme', 'insegel', 'sphinxawesome_theme',
        'basicstrap', 'cloud', 'sphinx_documatt_theme', 'groundwork',
        'sphinx_typo3_theme'
        )

html_theme = os.environ.get("confluence_theme", 'sphinx_material')
html_short_title = 'testkitdocs'
html_static_path = ['_static']
html_show_sourcelink = False
html_show_sphinx = False
html_show_copyright = False
