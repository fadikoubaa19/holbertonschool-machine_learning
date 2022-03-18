#!/usr/bin/env python3
"""task that initializes q_table"""


import numpy as np


def q_init(env):
    """env --> FrozenLakeEnv // return q_table using numpy of zeros"""
    s1 = env.action_space.n, a1 = env.observation_space.n

    # np.zeros return array filled with zeros
    return np.zeros((s1, a1))
