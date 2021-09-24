
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
        Create def __init__
        param: --> self, dm, h, hidden, drop_rate
        """
        super(EncoderBlock, self).__init__()
        self.mha = MultiHeadAttention(dm, h)
        self.dense_hidden = tf.keras.layers.Dense(units=hidden,
                                                  activation='relu')
        self.dense_output = tf.keras.layers.Dense(units=dm)

        self.layernorm1 = tf.keras.layers.LayerNormalization(epsilon=1e-6)
        self.layernorm2 = tf.keras.layers.LayerNormalization(epsilon=1e-6)

        self.dropout1 = tf.keras.layers.Dropout(drop_rate)
        self.dropout2 = tf.keras.layers.Dropout(drop_rate)

    def split_heads(self, x, batch_size):
        """
        split function
        param: --> self, x, batch_size:
        """
        x = tf.reshape(x, (batch_size, -1, self.h, self.depth))
        return tf.transpose(x, perm=[0, 2, 1, 3])

    def call(self, x, training, mask=None):
        """
        self, x, training
        """
        attention, _ = self.mha(x, x, x, mask)
        attention = self.dropout1(attention, training=training)
        out1 = self.layernorm1(x + attention)

        hidden = self.dense_hidden(out1)
        output = self.dense_output(hidden)

        dropout = self.dropout2(output, training=training)
        output = self.layernorm2(out1 + dropout)

        return output
