import tempfile

import tablign


def test_cli():
    infile = tempfile.NamedTemporaryFile().name

    with open(infile, "w") as f:
        f.write("""A  1.34  -214.1\nCCCC 55.534 1131.1""")

    outfile = tempfile.NamedTemporaryFile().name
    tablign.cli.main([infile, outfile])

    ref = """A     1.34  -214.1\nCCCC 55.534 1131.1"""
    with open(outfile, "r") as f:
        assert ref == f.read()
