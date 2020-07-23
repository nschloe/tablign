import argparse
import sys

from .__about__ import __version__
from .main import tablign


def main(argv=None):
    parser = _get_parser()
    args = parser.parse_args(argv)
    data = args.infile.read()

    out = tablign(data)

    args.outfile.write(out)
    return


def _get_parser():
    parser = argparse.ArgumentParser(description="Pretty-print ASCII tables.")

    parser.add_argument(
        "infile",
        nargs="?",
        type=argparse.FileType("r"),
        default=sys.stdin,
        help="input table file (default: stdin)",
    )

    parser.add_argument(
        "outfile",
        nargs="?",
        type=argparse.FileType("w"),
        default=sys.stdout,
        help="output table file (default: stdout)",
    )

    version_text = "tablign {}, Python {}.{}.{}".format(
        __version__,
        sys.version_info.major,
        sys.version_info.minor,
        sys.version_info.micro,
    )
    parser.add_argument("--version", "-v", action="version", version=version_text)

    return parser
