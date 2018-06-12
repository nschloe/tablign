# tablify

Pretty-prints your tables.

[![CircleCI](https://img.shields.io/circleci/project/github/nschloe/tablify/master.svg)](https://circleci.com/gh/nschloe/tablify/tree/master)
[![codecov](https://img.shields.io/codecov/c/github/nschloe/tablify.svg)](https://codecov.io/gh/nschloe/tablify)
[![Codacy grade](https://img.shields.io/codacy/grade/b23fbc2af9884315bd7d6275aa2629b6.svg)](https://app.codacy.com/app/nschloe/tablify/dashboard)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)
[![awesome](https://img.shields.io/badge/awesome-yes-brightgreen.svg)](https://github.com/nschloe/tablify)
[![PyPi Version](https://img.shields.io/pypi/v/tablify.svg)](https://pypi.python.org/pypi/tablify)
[![GitHub stars](https://img.shields.io/github/stars/nschloe/tablify.svg?logo=github&label=Stars)](https://github.com/nschloe/tablify)

tablify converts your input file
```
| A | 1.34|-214.1
|CCCC | 55.534|   1131.1|
```
into
```
| A    |  1.34  | -214.1 |
| CCCC | 55.534 | 1131.1 |
```
Column widths are unified across the table, decimal dots are aligned, and
tablify tries to be smart about column separators. Works for CSV, LaTeX,
Markdown etc.

### Usage from vim

Simply mark the table, and type
```
:'<,'>:!tablify
```

![](https://nschloe.github.io/tablify/tty-capture.gif)

### Installation

tablify is [available from the Python Package Index](https://pypi.python.org/pypi/tablify/), so with
```
pip install -U tablify
```
you can install/upgrade.

### Testing

To run the tests, simply check out this repository and run
```
pytest
```

### Distribution

To create a new release

1. bump the `__version__` number,

2. publish to PyPi and GitHub:
    ```
    $ make publish
    ```

### License
tablify is published under the [MIT license](https://en.wikipedia.org/wiki/MIT_License).
