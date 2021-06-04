#!/usr/bin/env python3
""" task 0"""
import tensorflow.keras as K


def build_model(nx, layers, activations, lambtha, keep_prob):
    """
    builds a neural network with the Keras library:
    """
    f = K.Sequential()
    kernel = K.regularizers.l2(lambtha)
    f.add(K.layers.Dense(layers[0], activation=activations[0],
                             input_dim=nx, kernel_regularizer=krnl,
                             name='dense'))
    for i in range(1, len(layers)):
        f.add(K.layers.Dropout(1 - keep_prob))
        f.add(K.layers.Dense(layers[i], activation=activations[i],
                                 kernel_regularizer=krnl,
                                 name='dense_'+str(i)))

    return f
