#!/usr/bin/env python3
"""Convolutions and pooling module"""
import numpy as np


def convolve_channels(images, kernel, padding='same', stride=(1, 1)):
    """convolve_channels"""
    m, inh, inw, c = images.shape
    a, b, x = kernel.shape
    f1, f2 = stride

    if padding == "valid":
        output_h = (inh - a) // f1 + 1
        output_w = (inw - b) // f2 + 1
        top, bot, lft, rgt, fnt, bck = (0, 0, 0, 0, 0, 0)

    elif padding == "same":
        output_h = inh
        output_w = inw

        padding_h = int(((inh - 1) * f1 + a - inh) / 2) + 1
        padding_w = int(((inw - 1) * f2 + b - inw) / 2) + 1

        top = padding_h
        bot = padding_h
        lft = padding_w
        rgt = padding_w

    else:
        ph, pw = padding
        output_h = (inh - a + 2 * ph) // f1 + 1
        output_w = (inw - b + 2 * pw) // f2 + 1
        top, bot = (ph, ph)
        lft, rgt = (pw, pw)

    _images = np.pad(
        array=images,
        pad_width=((0, 0), (top, bot), (lft, rgt), (0, 0)),
        mode="constant",
        constant_values=0
    )

    output = np.zeros((m, output_h, output_w))

    for i in range(output_h):
        for j in range(output_w):
            output[:, i, j] = np.sum(
                kernel * _images[
                    :,
                    i * f1:i * f1 + a,
                    j * f2:j * f2 + b
                ],
                axis=(1, 2, 3)
            )
    return output
