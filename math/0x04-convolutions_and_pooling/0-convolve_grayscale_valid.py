#!/usr/bin/env python3
"""first task"""
import numpy as np


def convolve_grayscale_valid(images, kernel):
    """convolve
    """
    m, input_h, input_w = images.shape
    a, b = kernel.shape

    output_h = int(np.floor(input_h - a + 1))
    output_w = int(np.floor(input_w - b + 1))
    output = np.zeros((m, output_h, output_w))
    for w in range(output_w):
        for h in range(output_h):
            output[:, h, w] = np.sum(
                kernel * images[:, h:h + a, w:w + b],
                axis=(1, 2)
            )
    return output
