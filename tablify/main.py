# -*- coding: utf-8 -*-
#
import numpy


def _one_align_char(arr, char):
    return numpy.all(1 == numpy.array([item.count(char) for item in arr]))


def tablify(data, align_char='.'):
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
    return data
