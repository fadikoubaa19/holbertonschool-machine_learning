#!/usr/bin/env python3
"""Task 0"""


import tensorflow as tf


def flip_image(image):
    """flips an image horizontally:"""
    return tf.image.flip_left_right(image)
