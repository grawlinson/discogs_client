"""discogs-api setup.py"""

import re
from os import path
from setuptools import setup, find_packages

PACKAGE_NAME = "discogs-api"
PACKAGE_DIR = "discogs_api"
HERE = path.abspath(path.dirname(__file__))
with open(path.join(HERE, "README.md"), encoding="utf-8") as fh:
    README = fh.read()
with open(path.join(HERE, PACKAGE_DIR, "__init__.py"), encoding="utf-8") as fh:
    VERSION = re.search('__version__ = \'([^"]+)\'', fh.read()).group(1)

setup(
    name=PACKAGE_NAME,
    version=VERSION,
    author="George Rawlinson",
    author_email="george@rawlinson.net.nz",
    description="Python interface to the Discogs REST API",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/grawlinson/python-discogs-api",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
    ],
    keywords="discogs api wrapper",
)
