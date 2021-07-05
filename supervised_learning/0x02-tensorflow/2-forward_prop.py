#!/usr/bin/env python3
""" 2-create_prop"""


def forward_prop(x, layer_sizes=[], activations=[]):
    """ create prop layer"""
    create_layer = __import__('1-create_layer').create_layer
    flak = create_layer(x, layer_sizes[0], activations[0])
    for i in range(1, len(layer_sizes)):
        flak = create_layer(flak, layer_sizes[i], activations[i])
    return (flak)
