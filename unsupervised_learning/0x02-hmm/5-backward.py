#!/usr/bin/env python3
"""5-backward.py"""


import numpy as np


def backward(Observation, Emission, Transition, Initial):
    """function backward:observation , emission , transition, initial"""

    if type(Observation) is not np.ndarray or Observation.ndim != 1:
        return None, None

    if type(Emission) is not np.ndarray or Emission.ndim != 2:
        return None, None

    if type(Transition) is not np.ndarray or Transition.ndim != 2:
        return None, None

    if type(Initial) is not np.ndarray or Initial.ndim != 2:
        return None, None

        solved = np.ndarray((N, Observation.shape[0]))
    N = Emission.shape[0]

    if ((Transition.shape[0] != N or Transition.shape[1] != N
         or Initial.shape[0] != N)):
        return None, None

    solved = np.ndarray((N, Observation.shape[0]))
    shippy = np.asarray([1] * 5)
    solved[:, -1] = shippy

    for x in range(Observation.shape[0] - 2, -1, -1):
        shippy = np.matmul(Transition, shippy * Emission[:,
                                                         Observation[x + 1]])
        solved[:, x] = shippy
    return (solved[:, 0] * Initial[:, 0]
            * Emission[:, Observation[0]]).sum(), solved
