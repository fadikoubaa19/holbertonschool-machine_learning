#!/usr/bin/env python3
"""
6-momentum
"""

import tensorflow as tf


def create_momentum_op(loss, alpha, beta1):
    """function that create momentum"""
    mom = tf.train.MomentumOptimizer(learning_rate=alpha, momentum=beta1)

    operation = train.minimize(operation)
    return operation
