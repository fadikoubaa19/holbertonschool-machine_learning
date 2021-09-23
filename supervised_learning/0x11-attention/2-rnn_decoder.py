#!/usr/bin/env python3
"""Create RNNEncoder class"""

import tensorflow as tf
SelfAttention = __import__('1-self_attention').SelfAttention


class RNNDecoder(tf.keras.layers.Layer):
    """Create RNNEncoder class
    param --> tf.keras.layers.layer"""
    def __init__(self, vocab, embedding, units, batch):
        """---------function __init__ ----------
        --> self // --> vocab // --> embeding--> units
        --> BATCH"""
        super(RNNDecoder, self).__init__()
        self.batch = batch
        self.units = units
        self.embedding = tf.keras.layers.Embedding(input_dim=vocab,
                                                   output_dim=embedding)

        self.gru = tf.keras.layers.GRU(units=units,
                                       recurrent_initializer='glorot_uniform',
                                       return_sequences=True,
                                       return_state=True)

        self.F = tf.keras.layers.Dense(units=vocab)

        self.attention = SelfAttention(units)

    def call(self, x, s_prev, hidden_states):
        """
        def call param -->
        param: ---> self, x, s_prev, hidden_states
        """
        vec, attention_weights = self.attention(s_prev,
                                                hidden_states)
        # Embedding vocan=b
        x = self.embedding(x)

        # Dimension along which to concatenate.
        x = tf.concat([tf.expand_dims(vec, 1), x], axis=-1)
        output, state = self.gru(x)
        output = tf.reshape(output, (-1, output.shape[2]))
        y = self.F(output)

        # retrun tensors
        return y, state
