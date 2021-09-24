#!/usr/bin/env python3
"""
"""
import tensorflow as tf
MultiHeadAttention = __import__('6-multihead_attention').MultiHeadAttention


class EncoderBlock(tf.keras.layers.Layer):
    """
    Class to create an encoder block for a transformer
    """

    def __init__(self, dm, h, hidden, drop_rate=0.1):
        """
        constructeur
        :param dm:
        :param h:
        :param hidden:
        :param drop_rate:
        """

        super(EncoderBlock, self).__init__()
        self.mha = MultiHeadAttention(dm, h)
        self.dense_hidden = tf.keras.layers.Dense(hidden, activation='relu')
        self.dense_output = tf.keras.layers.Dense(dm)
        self.layernorm1 = tf.keras.layers.LayerNormalization(epsilon=1e-6)
        self.layernorm2 = tf.keras.layers.LayerNormalization(epsilon=1e-6)
        self.dropout1 = tf.keras.layers.Dropout(drop_rate)
        self.dropout2 = tf.keras.layers.Dropout(drop_rate)

    def call(self, x, training, mask=None):
        """
        self, x, training
        """
        a_out, _ = self.mha(x, x, x, mask)
        a_out = self.dropout1(a_out, training=training)
        b_out = self.layernorm1(x + a_out)
        output = self.dense_hidden(b_out)
        output = self.dense_output(output)

        output = self.dropout2(output, training=training)
        out_put2 = self.layernorm2(b_out + output)

        return out_put2
