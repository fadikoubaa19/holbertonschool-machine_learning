#!/usr/bin/env python3
"""Convolutions and pooling module"""
import numpy as np


def convolve_grayscale_padding(images, kernel, padding):
    """convolution on grayscale images"""
    m, inh, inw = images.shape
    a, b = kernel.shape
    f1, f2 = padding

    output_h = inh - a + 2 * f1 + 1
    output_w = inw - b + 2 * f2 + 1

    padding_h = np.max(output_h - 1 + a - inh, 0)
    padding_w = np.max(output_w - 1 + b - inw, 0)

    top = int(np.floor(padding_h / 2))
    bot = padding_h - top
    lft = int(np.floor(padding_w / 2))
    rgt = padding_w - lft
    padded_images = np.pad(
        array=images,
        pad_width=((0, 0), (top, bot), (lft, rgt)),
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
