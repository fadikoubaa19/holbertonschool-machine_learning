#!/usr/bin/env python3
""" forward.py"""


import numpy as np


def forward(Observation, Emission, Transition, Initial):
    """
    function forward:observation, emission, transition, initial
    """

    if type(Observation) != np.ndarray:
        return None, None
    T = Observation.shape[0]

    if type(Emission) != np.ndarray:
        return None, None
    N = Emission.shape[0]

    if type(Transition) != np.ndarray:
        return None, None

    if type(Initial) != np.ndarray:
        return None, None

    F = np.zeros((N, T))
    F[:, 0] = np.multiply(Initial.T, Emission[:, Observation[0]])

    for i in range(1, T):
        for j in range(N):

            SDD = Transition[:, j]
            HDD = Emission[j, Observation[i]]
            F[j, i] = np.sum(F[:, i - 1] * HDD * SDD)

    P = F[:, -1:].sum()
    return P, F
