#!/usr/bin/env python3
"""Slice like a Ninja"""


def get_slice(slice_tpl) -> slice:
    """function that slices a matrix"""

    if slice_tpl and len(slice_tpl) == 1:
        a = None
        b = slice_tpl[0]
        c = None
    else:
        try:
            a = slice_tpl[0]
        except Exception:
            a = None
        try:
            b = slice_tpl[1]
        except Exception:
            b = None
        try:
            c = slice_tpl[2]
        except Exception:
            c = None
    return slice(a, b, c)


def np_slice(matrix, axes={}):
    """final function to slice axes"""
    s = []
    for j in range(len(matrix.shape)):
        s.append(get_slice(axes.get(j)))
    tpl_slicer = tuple(s)
    return matrix[tpl_slicer]
