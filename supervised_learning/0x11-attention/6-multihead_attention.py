#!/usr/bin/env python3
"""
Create multihead_attention
"""

import tensorflow as tf
sdp_attention = __import__('5-sdp_attention').sdp_attention


class MultiHeadAttention(tf.keras.layers.Layer):
    """
    Create class MultiHeadAttention
    """
    def __init__(self, dm, h):
        """function Init"""
        super().__init__()
        self.h = h
        self.dm = dm

        self.depth = dm // h

        self.Wq = tf.keras.layers.Dense(dm)
        self.Wk = tf.keras.layers.Dense(dm)
        self.Wv = tf.keras.layers.Dense(dm)

        self.linear = tf.keras.layers.Dense(dm)

    def split_heads(self, x, batch_size):
        """
        param : ---> self ,x ,batch_size
        """
        x = tf.reshape(x, (batch_size, -1, self.h, self.depth))
        return tf.transpose(x, perm=[0, 2, 1, 3])

    def call(self, Q, K, V, mask):
        """
        param: --> self, Q, K, V, mask:
        """
        batch_size = tf.shape(Q)[0]

        q = self.Wq(Q)
        k = self.Wk(K)
        v = self.Wv(V)

        q = self.split_heads(q, batch_size)
        k = self.split_heads(k, batch_size)
        v = self.split_heads(v, batch_size)

        attention_one, attention_weights = sdp_attention(q, k, v, mask)

        attention_one = tf.transpose(attention_one,
                                     perm=[0, 2, 1, 3])

        attention_two = tf.reshape(attention_one,
                                   (batch_size, -1, self.dm))

        output = self.linear(attention_one)

        return output, attention_weights
