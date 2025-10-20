# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os                                                                                                                                                                                                          
import sys                                                                                                                                                                                                         
sys.path.insert(0, os.path.abspath('../../src'))

from nanograz import __version__

project = 'NanoGrazDemo'
copyright = '2025, Dominik Brandstetter'
author = 'Dominik Brandstetter'
release = __version__

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.viewcode",
    "sphinx_rtd_theme",
    "sphinx.ext.napoleon",
]

templates_path = ['_templates']
exclude_patterns = []

autodoc_mock_imports = [
    "numpy",
]

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_sidebars = {
    "**": [
        "globaltoc.html",
        "relations.html",  # Show previous and next files
        "sourcelink.html",  # Show a link to the source on GitHub/GitLab/etc.
        "searchbox.html",  # Show a search box
    ]
}

html_theme = "sphinx_rtd_theme"
html_static_path = ['_static']
