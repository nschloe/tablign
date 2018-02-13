# -*- coding: utf-8 -*-
#
import numpy


def _one_align_char(arr, j, char):
    # return numpy.all(numpy.array([item.count(char) for item in arr]) == 1)
    for i, row in enumerate(arr):
        try:
            count = row[j].count(char)
        except IndexError:
            continue
        if count != 1:
            return False

    return True


def _max_col_length(data, j):
    max_col_length = 0
    for i, row in enumerate(data):
        try:
            max_col_length = max(max_col_length, len(row[j]))
        except IndexError:
            continue
    return max_col_length


def _guess_delimiter(string):
    # remove empty lines
    lines = [line for line in string.splitlines() if line.strip()]

    # possible delimeter in order of precedence
    possible_delimiters = '|&;,-'

    counts = numpy.zeros((len(lines), len(possible_delimiters)), dtype=int)
    for k, line in enumerate(lines):
        for i, delimiter in enumerate(possible_delimiters):
            counts[k, i] = line.count(delimiter)

    # Check if there is any delimiter that appears a constant nonzero number of
    # times per row.
    is_constant_per_col = numpy.all(counts == counts[0, :], axis=0)
    candidates = numpy.where(
        numpy.logical_and(is_constant_per_col, counts[0, :] > 0)
        )[0]

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
