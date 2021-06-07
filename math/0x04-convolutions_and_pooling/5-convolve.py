#!/usr/bin/env python3
"""Convolutions and pooling module"""
import numpy as np


def convolve(images, kernels, padding='same', stride=(1, 1)):
    """normal_convolve"""
    m, inh, inw, c = images.shape
    kh, kw, x, nc = kernels.shape
    ph, pw = stride

    if padding == "valid":
        output_h = (inh - kh) // ph + 1
        output_w = (inw - kw) // pw + 1
        top, bot, lft, rgt = (0, 0, 0, 0)

    elif padding == "same":
        output_h = inh
        output_w = inw

        padding_h = int(((inh - 1) * ph + kh - inh) / 2) + 1
        padding_w = int(((inw - 1) * pw + kw - inw) / 2) + 1

        top = padding_h
        bot = padding_h
        lft = padding_w
        rgt = padding_w

    else:
        ph, pw = padding
        output_h = (inh - kh + 2 * ph) // ph + 1
        output_w = (inw - kw + 2 * pw) // pw + 1
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
                    _images[:, i * f1:i * f1 + kh, j * f2:j * f2 + kw],
                    axis=(1, 2, 3)
                )
    return output
