<p align="center">
  <a href="https://github.com/nschloe/tablign"><img alt="tablign" src="https://nschloe.github.io/tablign/logo.svg" width="60%"></a>
  <p align="center">Aligns columns in your ASCII tables.</p>
</p>

[![PyPi Version](https://img.shields.io/pypi/v/tablign.svg?style=flat-square)](https://pypi.org/project/tablign)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/tablign.svg?style=flat-square)](https://pypi.org/pypi/tablign/)
[![GitHub stars](https://img.shields.io/github/stars/nschloe/tablign.svg?style=flat-square&logo=github&label=Stars&logoColor=white)](https://github.com/nschloe/tablign)
[![PyPi downloads](https://img.shields.io/pypi/dm/tablign.svg?style=flat-square)](https://pypistats.org/packages/tablign)

[![gh-actions](https://img.shields.io/github/workflow/status/nschloe/tablign/ci?style=flat-square)](https://github.com/nschloe/tablign/actions?query=workflow%3Aci)
[![codecov](https://img.shields.io/codecov/c/github/nschloe/tablign.svg?style=flat-square)](https://codecov.io/gh/nschloe/tablign)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg?style=flat-square)](https://github.com/psf/black)

Install with

```sh
pip install tablign
```


```sh
tablign in.txt out.txt
```

you can convert your input file

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
to be smart about column separators. Works for CSV, LaTeX, Markdown etc. By default,
`tablign` reads from stdin and writes to stdout, so you can use pipes with tablign, too:

```
head -n in.txt | tablign
```

### Usage from vim

Simply mark the table (shift-V), and type

```
:'<,'>:!tablign
```

![](https://nschloe.github.io/tablign/tty-capture.gif)


### Alternatives

[GNU's `column` command](https://man7.org/linux/man-pages/man1/column.1.html) is a mighty alternative:
```sh
column -t
```

See [here](https://stackoverflow.com/q/1229900/353337) for more alternatives.
