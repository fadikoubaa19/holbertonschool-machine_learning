#!/usr/bin/env python3
"""task 2"""

import tensorflow as tf


def rotate_image(image):
    """90 degree rotate"""
    return tf.image.rot90(image)
