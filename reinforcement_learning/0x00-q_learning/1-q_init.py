#!/usr/bin/env python3
"""task that initializes q_table"""


import numpy as np


def q_init(env):
    """env --> FrozenLakeEnv // return q_table using numpy of zeros"""
    action = (env.observation_space.n, env.action_space.n)

    # np.zeros return array filled with zeros
    return np.zeros((action))
