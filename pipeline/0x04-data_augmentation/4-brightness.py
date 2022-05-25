#!/usr/bin/env python3
"""task 4"""


import tensorflow as tf


def change_brightness(image, max_delta):
    """randomly changes the brightness of an image"""
    return tf.image.random_brightness(image, max_delta)
