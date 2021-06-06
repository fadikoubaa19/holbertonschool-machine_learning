#!/usr/bin/env python3
"""Convolution and pooling podule"""
import numpy as np


def convolve_grayscale_same(images, kernel):
    """task1"""
    m, inh, inw = images.shape
    a, b = kernel.shape

    output_h = inh
    output_w = inw

    padding_h = a // 2
    padding_w = b // 2

    padded_images = np.pad(
        array=images,
        pad_width=((0,), (padding_h,), (padding_w,)),
        mode="constant",
        constant_values=0
    )

    output = np.zeros((m, output_h, output_w))

    for i in range(output_h):
        for j in range(output_w):
            output[:, i, j] = np.sum(
                kernel * padded_images[:, i:i + a, j:j + b],
                axis=(1, 2)
            )
    return output
