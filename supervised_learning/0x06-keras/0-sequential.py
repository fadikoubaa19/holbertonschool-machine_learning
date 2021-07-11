#!/usr/bin/env python3
""" task 0"""
import tensorflow.keras as K


def build_model(nx, layers, activations, lambtha, keep_prob):

    """task0"""
    model = keras.Sequential()
    regularizer = keras.regularizers.l2(lambtha)
    model.add(keras.layers.Dense(units=layers[0],
                                 activation=activations[0],
                                 kernel_regularizer=regularizer,
                                 input_shape=(nx,)))
    for i in range(1, len(layers)):
        model.add(keras.layers.Dropout(1 - keep_prob))
        model.add(keras.layers.Dense(units=layers[i],
                                     activation=activations[i],
                                     kernel_regularizer=regularizer))
    return model
