import tempfile
from pathlib import Path

import tablign


def test_cli():
    with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir = Path(tmpdir)
        infile = tmpdir / "input.txt"

        with infile.open("w") as f:
            f.write("""A  1.34  -214.1\nCCCC 55.534 1131.1""")

        outfile = tmpdir / "output.txt"
        tablign.cli.main([str(infile), str(outfile)])

        ref = """A     1.34  -214.1\nCCCC 55.534 1131.1"""
        with outfile.open() as f:
            assert ref == f.read()
