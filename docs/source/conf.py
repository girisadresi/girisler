# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Giriş Adresleri'
copyright = '2023, Giriş Adresleri'
author = 'girisadresi'

release = '0.1'
version = '0.1.0'

language = "tr"

templates_path = ['_templates']

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]


html_css_files = [
    'css/custom.css',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'agogo'

html_show_sphinx = False

html_favicon = 'favicon.ico'

html_theme_options = {
    # Disable showing the sidebar. Defaults to 'false'
    'display_github': False,
    'nosidebar': True,
    'display_version': False
}
html_show_sourcelink = False
vcs_pageview_mode='view'