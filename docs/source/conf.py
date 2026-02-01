# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys
# Subimos dos niveles para llegar a la raíz del proyecto donde están los módulos
sys.path.insert(0, os.path.abspath('../../src'))

project = 'Laberinto de Texto'
copyright = '2026, Pablo Diaz, Rodrigo Sanmartin, Eudaldo Cal'
author = 'Pablo Diaz, Rodrigo Sanmartin, Eudaldo Cal'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode', # Opcional: permite ver tu código fuente desde el HTML
]

templates_path = ['_templates']
exclude_patterns = []

language = 'es'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
