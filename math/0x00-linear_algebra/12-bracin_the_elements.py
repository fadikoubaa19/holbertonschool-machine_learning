#!/usr/bin/env python3
"""
performs element-wise addition
"""


def np_elementwise(mat1, mat2):
    """functio that performs element-wise addition"""
    return ((mat1 + mat2), (mat1 - mat2),
            (mat1 * mat2), (mat1 / mat2))
