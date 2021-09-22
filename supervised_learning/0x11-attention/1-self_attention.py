#!/usr/bin/env python3
"""Create RNNEncoder class"""
import tensorflow as tf


class SelfAttention(tf.keras.layers.Layer):
    """RNNEncoder class"""
    def __init__(self, units):
        """-----Init function----"""
        super(SelfAttention, self).__init__()
        self.W = tf.keras.layers.Dense(units)
        self.U = tf.keras.layers.Dense(units)
        self.V = tf.keras.layers.Dense(1)

    def call(self, s_prev, hidden_states):
        """
        param : --->
        ---> self  ---> s_prev //  ---> hidden_states
        """

        # Tenserflow graph
        values = tf.expand_dims(s_prev, 1)

        # Building blocks
        points = self.V(tf.nn.tanh(self.W(values) + self.U(hidden_states)))

        # Turn numbers into probablities
        sof = tf.nn.softmax(points, axis=1)

        cal = sof * hidden_states
        cal = tf.reduce_sum(cal, axis=1)

        # Return y,s
        return cal, attention_weights
