#!/usr/bin/env python3
"""Load premade map from aiopen"""

import gym
import random
import time
from IPython.display import clear_output


def load_frozen_lake(desc=None, map_name=None, is_slippery=False):
    """ function that load frozenlake8x8"""
    return gym.make("FrozenLake-v1", desc=desc, map_name=map_name,
                    is_slippery=is_slippery)
