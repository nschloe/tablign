# tablign

Aligns columns in your ASCII tables.

[![CircleCI](https://img.shields.io/circleci/project/github/nschloe/tablign/master.svg?style=flat-square)](https://circleci.com/gh/nschloe/tablign/tree/master)
[![codecov](https://img.shields.io/codecov/c/github/nschloe/tablign.svg?style=flat-square)](https://codecov.io/gh/nschloe/tablign)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg?style=flat-square)](https://github.com/psf/black)
[![awesome](https://img.shields.io/badge/awesome-yes-brightgreen.svg?style=flat-square)](https://github.com/nschloe/tablign)
[![PyPi Version](https://img.shields.io/pypi/v/tablign.svg?style=flat-square)](https://pypi.python.org/pypi/tablign)
[![GitHub stars](https://img.shields.io/github/stars/nschloe/tablign.svg?style=flat-square&logo=github&label=Stars&logoColor=white)](https://github.com/nschloe/tablign)
[![PyPi downloads](https://img.shields.io/pypi/dm/tablign.svg?style=flat-square)](https://pypistats.org/packages/tablign)

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
Column widths are unified across the table, decimal dots are aligned, and tablign tries
to be smart about column separators. Works for CSV, LaTeX, Markdown etc.

### Usage from vim

Simply mark the table (shift-V), and type
```
:'<,'>:!tablign
```

![](https://nschloe.github.io/tablign/tty-capture.gif)

### Installation

tablign is [available from the Python Package
Index](https://pypi.python.org/pypi/tablign/), so with
```
pip3 install -U tablign
```
you can install/upgrade.

### Testing

To run the tests, simply check out this repository and run
```
pytest
```

### License
tablign is published under the [MIT license](https://en.wikipedia.org/wiki/MIT_License).
