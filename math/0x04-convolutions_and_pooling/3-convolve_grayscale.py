#!/usr/bin/env python3
"""task 3"""
import numpy as np


def convolve_grayscale(images, kernel, padding='same', stride=(1, 1)):
    """performs a convolution on grayscale images"""
    m, inh, inw = images.shape
    a, b = kernel.shape
    c, d = stride

    if padding == "valid":
        output_h = (inh - a) // c + 1
        output_w = (inw - b) // d + 1
        top, bot, lft, rgt = (0, 0, 0, 0)

    elif padding == "same":
        output_h = inh
        output_w = inw

        padding_h = int(((inh - 1) * c + a - inh) / 2) + 1
        padding_w = int(((inw - 1) * d + b - inw) / 2) + 1

        top = padding_h
        bot = padding_h
        lft = padding_w
        rgt = padding_w

    else:
        f1, f2 = padding
        output_h = (inh - a + 2 * f1) // c + 1
        output_w = (inw - b + 2 * f2) // d + 1
        top, bot = (f1, f1)
        lft, rgt = (f2, f2)

    _images = np.pad(
        array=images,
        pad_width=((0, 0), (top, bot), (lft, rgt)),
        mode="constant",
        constant_values=0
    )

    output = np.zeros((m, output_h, output_w))

    for i in range(output_h):
        for j in range(output_w):
            output[:, i, j] = np.sum(
                kernel * _images[
                    :,
                    i * c:i * c + a,
                    j * d:j * d + b
                ],
                axis=(1, 2)
            )
    return output
