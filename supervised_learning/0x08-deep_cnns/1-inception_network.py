#!/usr/bin/env python3
""" function icep_network """

import tensorflow.keras as K

inception_block = __import__('0-inception_block').inception_block


def inception_network():
    """
    function that build incp net
    """
    initializer = K.initializers.he_normal(seed=None)

    X = K.Input(shape=(224, 224, 3))

    my_block = K.layers.Conv2D(filters=64,
                               kernel_size=(7, 7),
                               strides=(2, 2),
                               padding='same',
                               activation='relu',
                               kernel_initializer=initializer,
                               )(X)

    my_block = K.layers.MaxPool2D(pool_size=(3, 3),
                                  padding='same',
                                  strides=(2, 2)
                                  )(my_block)

    my_block = K.layers.Conv2D(filters=64,
                               kernel_size=(1, 1),
                               strides=(1, 1),
                               padding='same',
                               activation='relu',
                               kernel_initializer=initializer,
                               )(my_block)

    my_block = K.layers.Conv2D(filters=192,
                               kernel_size=(3, 3),
                               strides=(1, 1),
                               padding='same',
                               activation='relu',
                               kernel_initializer=initializer,
                               )(my_block)

    my_block = K.layers.MaxPool2D(pool_size=(3, 3),
                                  padding='same',
                                  strides=(2, 2)
                                  )(my_block)

    my_block = inception_block(my_block, [64, 96, 128, 16, 32, 32])

    my_block = inception_block(my_block, [128, 128, 192, 32, 96, 64])

    my_block = K.layers.MaxPool2D(pool_size=(3, 3),
                                  padding='same',
                                  strides=(2, 2)
                                  )(my_block)

    my_block = inception_block(my_block, [192, 96, 208, 16, 48, 64])
    my_block = inception_block(my_block, [160, 112, 224, 24, 64, 64])
    my_block = inception_block(my_block, [128, 128, 256, 24, 64, 64])
    my_block = inception_block(my_block, [112, 144, 288, 32, 64, 64])
    my_block = inception_block(my_block, [256, 160, 320, 32, 128, 128])

    my_block = K.layers.MaxPool2D(pool_size=(3, 3),
                                  padding='same',
                                  strides=(2, 2)
                                  )(my_block)

    my_block = inception_block(my_block, [256, 160, 320, 32, 128, 128])
    my_block = inception_block(my_block, [384, 192, 384, 48, 128, 128])

    my_block = K.layers.AveragePooling2D(pool_size=(7, 7),
                                         padding='same'
                                         )(my_block)

    my_block = K.layers.Dropout(rate=0.4)(my_block)

    my_block = K.layers.Dense(units=1000,
                              activation='softmax',
                              kernel_initializer=initializer,
                              )(my_block)

    model = K.models.Model(inputs=X, outputs=my_l)

    return model
