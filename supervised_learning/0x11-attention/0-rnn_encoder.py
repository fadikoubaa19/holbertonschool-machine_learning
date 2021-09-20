#!/usr/bin/env python3
"""Create RNNEncoder class"""
import tensorflow as tf


class RNNEncoder(tf.keras.layers.Layer):
    """param: --> self , vocab, embedding, units, batch"""
    def __init__(self, vocab, embedding, units, batch):
        """Class constructor"""
        super(RNNEncoder, self).__init__()
        self.batch = batch
        self.units = units
        self.embedding = tf.keras.layers.Embedding(vocab, embedding)
        self.gru = tf.keras.layers.GRU(units,
                                       recurrent_initializer='glorot_uniform',
                                       return_sequences=True,
                                       return_state=True)

    def initialize_hidden_state(self):
        """
        param:---> self
        """
        initializer = tf.keras.initializers.Zeros()
        values = initializer(shape=(self.batch, self.units))
        return values

    def call(self, x, initial):
        """
        param:--> self, x, initial
        """
        input = self.embedding(x)
        outputs, hidden = self.gru(input, initial_state=initial)
        return outputs, hidden
