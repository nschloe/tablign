# -*- coding: utf-8 -*-
#
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


if __name__ == '__main__':
    test_tablify()
