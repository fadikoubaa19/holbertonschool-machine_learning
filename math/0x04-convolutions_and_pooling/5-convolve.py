#!/usr/bin/env python3
"""task 5"""
import numpy as np


def convolve(images, kernels, padding='same', stride=(1, 1)):
    """Performs a convolution"""
    m, input_h, input_w, c = images.shape
    kh, kw, fd, nc = kernels.shape
    sh, sw = stride

    if padding == "valid":
        output_h = (input_h - kh) // sh + 1
        output_w = (input_w - kw) // sw + 1
        top, bot, lft, rgt = (0, 0, 0, 0)

    elif padding == "same":
        output_h = input_h
        output_w = input_w

        padding_h = int(((input_h - 1) * sh + kh - input_h) / 2) + 1
        padding_w = int(((input_w - 1) * sw + kw - input_w) / 2) + 1

        top = padding_h
        bot = padding_h
        lft = padding_w
        rgt = padding_w

    else:
        ph, pw = padding
        output_h = (input_h - kh + 2 * ph) // sh + 1
        output_w = (input_w - kw + 2 * pw) // sw + 1
        top, bot = (ph, ph)
        lft, rgt = (pw, pw)

    _images = np.pad(
        array=images,
        pad_width=((0, 0), (top, bot), (lft, rgt), (0, 0)),
        mode="constant",
        constant_values=0
    )

    output = np.zeros((m, output_h, output_w, c))

    for i in range(output_h):
        for j in range(output_w):
            for k in range(nc):
                output[:, i, j, k] = np.sum(
                    kernels[:, :, :, k] *
                    _images[:, i * sh:i * sh + kh, j * sw:j * sw + kw],
                    axis=(1, 2, 3)
                )
    return output
