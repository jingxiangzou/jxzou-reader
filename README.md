# Words in the front 
This is the 0.0.1 version of my test package of the library

# Real Python Feed Reader

The Real Python Feed Reader is a basic [web feed](https://en.wikipedia.org/wiki/Web_feed) reader that can download the latest Real Python tutorials from the [Real Python feed](https://realpython.com/contact/#rss-atom-feed).

For more information see the tutorial [How to Publish an Open-Source Python Package to PyPI](https://realpython.com/pypi-publish-python-package/) on Real Python.

## Installation

You can install the Real Python Feed Reader from [PyPI](https://pypi.org/project/realpython-reader/):

    python -m pip install realpython-reader

The reader is supported on Python 3.7 and above. Older versions of Python, including Python 2.7, are supported by version 1.0.0 of the reader.

## How to use

The Real Python Feed Reader is a command line application, named `realpython`. To see a list of the [latest Real Python tutorials](https://realpython.com/), call the program without any arguments:

    $ realpython
    The latest tutorials from Real Python (https://realpython.com/)
     0 How to Publish an Open-Source Python Package to PyPI
     1 Python "while" Loops (Indefinite Iteration)
     2 Writing Comments in Python (Guide)
     3 Setting Up Python for Machine Learning on Windows
     4 Python Community Interview With Michael Kennedy
     5 Practical Text Classification With Python and Keras
     6 Getting Started With Testing in Python
     7 Python, Boto3, and AWS S3: Demystified
     8 Python's range() Function (Guide)
     9 Python Community Interview With Mike Grouchy
    10 How to Round Numbers in Python
    11 Building and Documenting Python REST APIs With Flask and Connexion – Part 2
    12 Splitting, Concatenating, and Joining Strings in Python
    13 Image Segmentation Using Color Spaces in OpenCV + Python
    14 Python Community Interview With Mahdi Yusuf
    15 Absolute vs Relative Imports in Python
    16 Top 10 Must-Watch PyCon Talks
    17 Logging in Python
    18 The Best Python Books
    19 Conditional Statements in Python

To read one particular tutorial, call the program with the numerical ID of the tutorial as a parameter:

    $ realpython 0
    # How to Publish an Open-Source Python Package to PyPI

    Python is famous for coming with batteries included. Sophisticated
    capabilities are available in the standard library. You can find modules for
    working with sockets, parsing CSV, JSON, and XML files, and working with
    files and file paths.

    However great the packages included with Python are, there are many
    fantastic projects available outside the standard library. These are most
    often hosted at the Python Packaging Index (PyPI), historically known as the
    Cheese Shop. At PyPI, you can find everything from Hello World to advanced
    deep learning libraries.

    [... The full text of the article ...]

You can also call the Real Python Feed Reader in your own Python code, by importing from the `reader` package:

    >>> from reader import feed
    >>> feed.get_titles()
    ['How to Publish an Open-Source Python Package to PyPI', ...]


# 竟翔的话

pyproject.toml is used for package configuration, specifying properties of the package including: (I shall just paste the code below):

    # pyproject.toml

    [build-system]
    requires      = ["setuptools>=61.0.0", "wheel"]
    build-backend = "setuptools.build_meta"

    [project]
    ## name specifies the name of your package as it will appear on PyPI.
    name = "jxzou-reader" 

    ## version sets the current version of your package.
    version = "1.0.0" 

    description = "Read the latest Real Python tutorials"
    readme = "README.md"
    authors = [{ name = "Jingxiang Zou", email = "jxzou@bu.edu" }]
    license = { file = "LICENSE" }

    ## classifiers describes your project using a list of classifiers. You should use these as they make your project more searchable.

    classifiers = [
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ]

    keywords = ["feed", "reader", "tutorial"]

    ## dependencies lists any dependencies your package has to third-party libraries. reader depends on feedparser, html2text, and tomli, so they’re listed here.

    dependencies = [
        "feedparser >= 5.2.0",
        "html2text",
        'tomli; python_version < "3.11"',
    ]
    requires-python = ">=3.9"

    [project.optional-dependencies]
    dev = ["black", "bumpver", "isort", "pip-tools", "pytest"]

    ## project.urls adds links that you can use to present additional information about your package to your users. You can include several links here.

    [project.urls]
    Homepage = "https://github.com/realpython/reader"

    ## project.scripts creates command-line scripts that call functions within your package. Here, the new realpython command calls main() within the reader.__main__ module.

    [project.scripts]
    realpython = "reader.__main__:main"


## TIPS on versioning: 

Semantic versioning is a good default scheme to use, although it’s not perfect. You specify the version as three numerical components, for instance 1.2.3. The components are called MAJOR, MINOR, and PATCH, respectively. The following are recommendations about when to increment each component:

1. Increment the MAJOR version when you make incompatible API changes.
2. Increment the MINOR version when you add functionality in a backwards compatible manner.
3. Increment the PATCH version when you make backwards compatible bug fixes. (Source)

## what is a virtual environment?

A virtual environment is (amongst other things): 
Used to contain a specific Python interpreter and software libraries and binaries which are needed to support a project (library or application).

## Setting up MANIFEST to ensure files are included in the project 
Sometimes, you’ll have files inside your package that aren’t source code files. 
Examples include data files, binaries, documentation, and(as you have in this example)configuration files.

To make sure such files are included when your project is built, you use a manifest file. For many projects, you don’t need to worry about the manifest: by default, Setuptools includes all source code files and README files in the build.

If you have other resource files and need to update the manifest, then you need to create a file named MANIFEST.in next to pyproject.toml in your project’s base directory. This file specifies rules for which files to include and which files to exclude:

### MANIFEST.in
include src/reader/*.toml

This example will include all .toml files in the src/reader/ directory. In effect, this is the configuration file.
See the documentation for more information about setting up your manifest. The check-manifest tool can also be useful for working with MANIFEST.in.

## License your package 
If you’re sharing your package with others, then you need to add a license to your package that explains how others are allowed to use your package. 
For example, reader is distributed according to the MIT license.

**Licenses are legal documents, and you typically don’t want to write your own.
Instead, you should choose one of the many licenses already available.**

You should add a file named LICENSE to your project that contains the text of the license you choose. 
You can then reference this file in pyproject.toml to make the license visible on PyPI.

## What is a Virtual Environment (venv)?
 "Virtual Environment". It provides an isolated environment wherein you can download a different version of python packages and run it for your project. Hence, do not put anything inside your virtual environment. Keep it clean.

 
