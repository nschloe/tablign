# -*- coding: utf-8 -*-
#


def _one_align_char(arr, j, char):
    for _, row in enumerate(arr):
        try:
            count = row[j].count(char)
        except IndexError:
            continue
        if count != 1:
            return False
    return True


def _max_col_length(data, j):
    max_col_length = 0
    for _, row in enumerate(data):
        try:
            max_col_length = max(max_col_length, len(row[j]))
        except IndexError:
            continue
    return max_col_length


def _guess_delimiter(lines):
    # remove empty lines
    lines = [line for line in lines if line.strip()]

    for delimiter in '|&;,':
        counts = [line.count(delimiter) for _, line in enumerate(lines)]
        # Check if the delimiter appears more than once in every line.
        if all([item > 1 for item in counts]):
            return delimiter

    return None


def _align(data, j, align_char):
    num_char_before_dot = 0
    num_char_after_dot = 0
    for i, row in enumerate(data):
        try:
            item = data[i][j]
        except IndexError:
            continue
        before, after = item.split(align_char)
        num_char_before_dot = max(num_char_before_dot, len(before))
        num_char_after_dot = max(num_char_after_dot, len(after))

    for i, row in enumerate(data):
        try:
            item = data[i][j]
        except IndexError:
            continue

        before, after = item.split(align_char)
        data[i][j] = (
            ' ' * (num_char_before_dot - len(before)) +
            item +
            ' ' * (num_char_after_dot - len(after))
            )
    return data


def tablify(string, align_char='.', delimiter=None):
    lines = string.splitlines()

    if delimiter is None:
        delimiter = _guess_delimiter(lines)

    data = [line.split(delimiter) for line in lines]

    # remove leading and trailing whitespace from entries
    for i, row in enumerate(data):
        for j, item in enumerate(row):
            data[i][j] = item.strip()

    max_num_cols = max([len(data[i]) for i in range(len(data))])

    for j in range(max_num_cols):
        if _one_align_char(data, j, align_char):
            data = _align(data, j, align_char)
        else:
            max_length = _max_col_length(data, j)
            # append spaces to make all entries equally long
            for i, row in enumerate(data):
                try:
                    data[i][j] = data[i][j].ljust(max_length)
                except IndexError:
                    continue

    sep = ' {} '.format(delimiter) if delimiter else ' '

    # Only strip trailing whitespace if the delimiter is None.
    strp = str.rstrip if delimiter is None else str.strip

    return '\n'.join([strp(sep.join(row)) for _, row in enumerate(data)])
