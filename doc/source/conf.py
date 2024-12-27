# step1 : sphinx-quickstart
# step2 : 替换conf内容
# step2 : 修改index.rst结构
# step3 : sphinx-apidoc -o source ../../lb_toolkits/
# step4 : make html
# step5 : make clean


# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------
import os.path
import sys
import re
import datetime

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
sys.path.append(os.path.abspath('../../'))
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
# -- Project information -----------------------------------------------------

project = 'lb_toolkits'
copyright = u'2020-{}, Lee'.format(datetime.datetime.utcnow().strftime("%Y"))
author = 'Lee'

# The full version, including alpha/beta/rc tags

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.

# from lb_toolkits.version import get_versions
# version = get_versions()['version']
# del get_versions

with open(os.path.join("../..", "lb_toolkits", "__init__.py"), "rt") as fp:
    version = re.search(r'__version__\s*=\s*"(\S+)"', fp.read()).group(1)

# The full version, including alpha/beta/rc tags.
release = version


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx.ext.coverage",
]

apidoc_module_dir = "../../lb_toolkits"
apidoc_output_dir = "api"
apidoc_excluded_paths = [
    'utils/hdfpro.py',
]
apidoc_separate_modules = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']


# The suffix of source filenames.
source_suffix = ".rst"

# The master toctree document.
master_doc = "index"



# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'zh_CN'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns =  ["_build", "Thumbs.db", ".DS_Store"]

# If true, '()' will be appended to :func: etc. cross-reference text.
add_function_parentheses = True


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ['_static']

# Output file base name for HTML help builder.
htmlhelp_basename = "lb_toolkitsdoc"

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (
        "index",
        "lb_toolkits.tex",
        "lb_toolkits Documentation",
        "lb_toolkits Developers",
        "manual",
    )
]

on_rtd = os.environ.get('READTHEDOCS', None) == 'True'
if on_rtd:
    latex_elements = {
        # The paper size ('letterpaper' or 'a4paper').
        #'papersize': 'letterpaper',
        # The font size ('10pt', '11pt' or '12pt').
        #'pointsize': '10pt',
        # Additional stuff for the LaTeX preamble.
        'preamble': r'''
    \hypersetup{unicode=true}
    \usepackage{CJKutf8}
    \DeclareUnicodeCharacter{00A0}{\nobreakspace}
    \DeclareUnicodeCharacter{2203}{\ensuremath{\exists}}
    \DeclareUnicodeCharacter{2200}{\ensuremath{\forall}}
    \DeclareUnicodeCharacter{2286}{\ensuremath{\subseteq}}
    \DeclareUnicodeCharacter{2713}{x}
    \DeclareUnicodeCharacter{27FA}{\ensuremath{\Longleftrightarrow}}
    \DeclareUnicodeCharacter{221A}{\ensuremath{\sqrt{}}}
    \DeclareUnicodeCharacter{221B}{\ensuremath{\sqrt[3]{}}}
    \DeclareUnicodeCharacter{2295}{\ensuremath{\oplus}}
    \DeclareUnicodeCharacter{2297}{\ensuremath{\otimes}}
    \begin{CJK}{UTF8}{gbsn}
    \AtEndDocument{\end{CJK}}
    ''',
    }
else:
    latex_elements = {
        'papersize' : 'a4paper',
        'utf8extra' : '',
        'inputenc'  : '',
        'babel'     : r'''\usepackage[english]{babel}''',
        'preamble' : r'''
        \usepackage{ctex}
        ''',
    }

# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ("index", "lb_toolkits", "lb_toolkits Documentation", ["Lee"], 1)
]

# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (
        "index",
        "lb_toolkits",
        "lb_toolkits Documentation",
        "Lee",
        "lb_toolkits",
        "Copernicus data search and download.",
        "Miscellaneous",
    )
]

# https://stackoverflow.com/a/46284013/2997179
# Avoid listing "object" as base class
from sphinx.ext.autodoc import ClassDocumenter, _

add_line = ClassDocumenter.add_line
line_to_delete = _("Bases: %s") % ":class:`object`"


def add_line_no_object_base(self, text, *args, **kwargs):
    if text.strip() == line_to_delete:
        return
    add_line(self, text, *args, **kwargs)


add_directive_header = ClassDocumenter.add_directive_header


def add_directive_header_no_object_base(self, *args, **kwargs):
    self.add_line = add_line_no_object_base.__get__(self)
    result = add_directive_header(self, *args, **kwargs)
    del self.add_line
    return result


ClassDocumenter.add_directive_header = add_directive_header_no_object_base