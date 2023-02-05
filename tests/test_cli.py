import tempfile
from pathlib import Path

import tablign


def test_cli():
    infile = Path(tempfile.NamedTemporaryFile().name)

    with infile.open("w") as f:
        f.write("""A  1.34  -214.1\nCCCC 55.534 1131.1""")

    outfile = Path(tempfile.NamedTemporaryFile().name)
    tablign.cli.main([infile, outfile])

    ref = """A     1.34  -214.1\nCCCC 55.534 1131.1"""
    with outfile.open() as f:
        assert ref == f.read()
