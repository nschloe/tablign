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


def _guess_delimiter(string):
    # remove empty lines
    lines = [line for line in string.splitlines() if line.strip()]

    # possible delimeter in order of precedence
    possible_delimiters = '|&;'

    counts = [
        [0 for _ in range(len(lines))]
        for _ in range(len(possible_delimiters))
        ]
    for k, line in enumerate(lines):
        for i, delimiter in enumerate(possible_delimiters):
            counts[i][k] = line.count(delimiter)

    # Check if there is any delimiter appears more than once per line.
    is_candidate = [all([item > 1 for item in row]) for row in counts]
    candidates = [i for i, x in enumerate(is_candidate) if x]

    if len(candidates) > 0:
        return possible_delimiters[candidates[0]]
    return None


def tablify(string, align_char='.', delimiter=None):
    if delimiter is None:
        delimiter = _guess_delimiter(string)

    data = [line.split(delimiter) for line in string.splitlines()]

    # remove leading and trailing whitespace from entries
    for i, row in enumerate(data):
        for j, item in enumerate(row):
            data[i][j] = item.strip()

    max_num_cols = max([len(data[i]) for i in range(len(data))])

    for j in range(max_num_cols):
        if _one_align_char(data, j, align_char):
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
        else:
            max_length = _max_col_length(data, j)
            # append spaces to make all entries equally long
            for i, row in enumerate(data):
                try:
                    data[i][j] += ' ' * (max_length - len(data[i][j]))
                except IndexError:
                    continue

    sep = ' {} '.format(delimiter) if delimiter else ' '

    return '\n'.join([sep.join(row).rstrip() for _, row in enumerate(data)])
