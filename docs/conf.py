import os
import sys

sys.path.insert(0, os.path.abspath("../"))

project = "nodriver"
copyright = "2023, Author"
author = "Author"


extensions = [
    "sphinx.ext.napoleon",
    "sphinx.ext.autodoc",
    "sphinx.ext.viewcode",
    "sphinx_autodoc_typehints",
    "sphinx.ext.doctest",
    "sphinx.ext.intersphinx",
    "sphinx_markdown_builder",
    "sphinxcontrib.video",
]

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
}

exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
add_module_names = False
language = "en"

default_role = "any"
autodoc_member_order = "bysource"
# autodoc_typehints = "none"
# autoclass_content = "both"
# Don't show class signature with the class' name.
# autodoc_class_signature = "separated"

pygments_style = "sphinx"
pygments_dark_style = "monokai"
html_static_path = ["_static"]
html_theme = "furo"
html_css_files = [
    "./custom.css",
]
html_sidebars = {
    "**": [
        "sidebar/scroll-start.html",
        "sidebar/brand.html",
        "sidebar/search.html",
        "sidebar/navigation.html",
        "sidebar/ethical-ads.html",
        "sidebar/scroll-end.html",
    ]
}
html_theme_options = {
    "dark_css_variables": {
        "color-brand-primary": "#8eefba",
        "color-background-primary": "#111112",
        "color-problematic": "#e7aeae",
    },
}
