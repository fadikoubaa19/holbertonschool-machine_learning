#!/usr/bin/env python3
""" 2-create_prop"""

import tensorflow as tf


create_layer = __import__('1-create_layer').create_layer


def forward_prop(x, layer_sizes=[], activations=[]):
    """ create prop layer"""
    pred = x
    for i in range(len(layer_sizes)):
        pred = create_layer(pred, layer_sizes[i],
                            activation=activations[i])
    return pred
