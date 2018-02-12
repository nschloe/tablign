# -*- coding: utf-8 -*-
#
import numpy


def _one_align_char(arr, char):
    return numpy.all(numpy.array([item.count(char) for item in arr]) == 1)


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
    data = numpy.loadtxt(string.splitlines(), dtype=str, delimiter=delimiter)

    # remove leading and trailing whitespace from entries
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            data[i][j] = data[i][j].strip()

    for j in range(data.shape[1]):
        if _one_align_char(data[:, j], align_char):
            num_char_before_dot = 0
            num_char_after_dot = 0
            for item in data[:, j]:
                before, after = item.split(align_char)
                num_char_before_dot = max(num_char_before_dot, len(before))
                num_char_after_dot = max(num_char_after_dot, len(after))

            for i in range(len(data[:, j])):
                before, after = data[i, j].split(align_char)
                data[i, j] = (
                    ' ' * (num_char_before_dot - len(before)) +
                    data[i, j] +
                    ' ' * (num_char_after_dot - len(after))
                    )
        else:
            max_length = max([len(item) for item in data[:, j]])
            # append spaces to make all entries equally long
            for i in range(len(data[:, j])):
                data[i, j] += ' ' * (max_length - len(data[i, j]))

    sep = ' {} '.format(delimiter) if delimiter else ' '

    return '\n'.join([sep.join(data[i]) for i in range(data.shape[0])])
