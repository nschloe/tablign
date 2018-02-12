# -*- coding: utf-8 -*-
#
import pytest

import tablify


def test_tablify():
    data = '''
    A  1.34  -214.1
    CCCC 55.534 1131.1
    '''
    ref = '''A     1.34  -214.1
CCCC 55.534 1131.1'''

    assert tablify.tablify(data) == ref
    return


@pytest.mark.parametrize('sep_char', [
    ','
    ])
def test_column_seps(sep_char):
    data = '''
    A  {} 1.34    {} -214.1
    CCCC {}        55.534 {} 1131.1'''.format(*(4 * sep_char))
    ref = '''A    {}  1.34  {} -214.1
CCCC {} 55.534 {} 1131.1'''.format(*(4 * sep_char))

    assert tablify.tablify(data) == ref
    return


if __name__ == '__main__':
    test_column_seps(',')
