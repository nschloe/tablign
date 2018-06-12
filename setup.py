# -*- coding: utf-8 -*-
#
import codecs
import os

from setuptools import setup, find_packages

# https://packaging.python.org/single_source_version/
base_dir = os.path.abspath(os.path.dirname(__file__))
about = {}
with open(os.path.join(base_dir, "tablify", "__about__.py"), "rb") as f:
    # pylint: disable=exec-used
    exec(f.read(), about)


def read(fname):
    try:
        content = codecs.open(os.path.join(base_dir, fname), encoding="utf-8").read()
    except IOError:
        content = ""
    return content


setup(
    name="tablify",
    version=about["__version__"],
    packages=find_packages(),
    url="https://github.com/nschloe/tablify",
    download_url="https://pypi.python.org/pypi/tablify",
    author=about["__author__"],
    author_email=about["__author_email__"],
    install_requires=["pipdate"],
    description="tools for color models",
    long_description=read("README.rst"),
    license=about["__license__"],
    classifiers=[
        about["__license__"],
        about["__status__"],
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Topic :: Text Editors :: Text Processing",
        "Topic :: Text Processing",
        "Topic :: Text Processing :: Filters",
        "Topic :: Text Processing :: Markup",
        "Topic :: Text Processing :: Markup :: LaTeX",
        "Topic :: Utilities",
    ],
)
