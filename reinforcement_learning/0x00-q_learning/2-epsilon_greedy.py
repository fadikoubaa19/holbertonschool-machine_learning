#!/usr/bin/env python3
"""task 3"""

import numpy as np


def epsilon_greedy(Q, state, epsilon):
    """
    """

    # Determine if i need to exploite or explore
    if np.random.uniform(0, 1) < epsilon:

        # Exploring:
        # picking next action using numpy.random.randint:
        next_move = np.random.randint(Q.shape[1])
    else:
        next_move = np.argmax(Q[state, :])
    return next_move
