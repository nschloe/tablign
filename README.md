# tablign

Aligns columns in your ASCII tables.

[![CircleCI](https://img.shields.io/circleci/project/github/nschloe/tablign/master.svg)](https://circleci.com/gh/nschloe/tablign/tree/master)
[![codecov](https://img.shields.io/codecov/c/github/nschloe/tablign.svg)](https://codecov.io/gh/nschloe/tablign)
[![Codacy grade](https://img.shields.io/codacy/grade/b23fbc2af9884315bd7d6275aa2629b6.svg)](https://app.codacy.com/app/nschloe/tablign/dashboard)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)
[![awesome](https://img.shields.io/badge/awesome-yes-brightgreen.svg)](https://github.com/nschloe/tablign)
[![PyPi Version](https://img.shields.io/pypi/v/tablign.svg)](https://pypi.python.org/pypi/tablign)
[![GitHub stars](https://img.shields.io/github/stars/nschloe/tablign.svg?logo=github&label=Stars)](https://github.com/nschloe/tablign)

tablign converts your input file
```
| A | 1.34|-214.1|
|CCCC | 55.534|   1131.1|
```
into
```
| A    |  1.34  | -214.1 |
| CCCC | 55.534 | 1131.1 |
```
Column widths are unified across the table, decimal dots are aligned, and
tablign tries to be smart about column separators. Works for CSV, LaTeX,
Markdown etc.

### Usage from vim

Simply mark the table, and type
```
:'<,'>:!tablign
```

![](https://nschloe.github.io/tablign/tty-capture.gif)

### Installation

tablign is [available from the Python Package Index](https://pypi.python.org/pypi/tablign/), so with
```
pip install -U tablign
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
tablign is published under the [MIT license](https://en.wikipedia.org/wiki/MIT_License).
