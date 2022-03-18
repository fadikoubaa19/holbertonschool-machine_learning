#!/usr/bin/env python3
"""Load premade map from aiopen"""

import gym


def load_frozen_lake(desc=None, map_name=None, is_slippery=False):
    """ function that load frozenlake8x8"""

    return gym.make("FrozenLake-v0", desc=desc, map_name=map_name)
