#!/usr/bin/env python3
""" viterbi"""


import numpy as np


def viterbi(Observation, Emission, Transition, Initial):
    """
    function viterbi
    """

    if type(Observation) is not np.ndarray or Observation.ndim != 1:
        return None, None

    if type(Emission) is not np.ndarray or Emission.ndim != 2:
        return None, None

    if type(Transition) is not np.ndarray or Transition.ndim != 2:
        return None, None

    if type(Initial) is not np.ndarray or Initial.ndim != 2:
        return None, None
    N = Emission.shape[0]

    if ((Transition.shape[0] != N or Transition.shape[1] != N
         or Initial.shape[0] != N)):
        return None, None

    solved = np.ndarray((N, Observation.shape[0]))
    calc = Initial
    major = np.ndarray((N, Observation.shape[0] - 1))

    for obs in range(0, Observation.shape[0]):
        calc = calc * Emission[:, [Observation[obs]]]
        major[:, obs - 1] = calc.argmax(axis=1)
        calc = calc.max(axis=1)
        solved[:, obs] = calc
        calc = Transition.T * calc
    prev = solved[:, -1].argmax()
    ship = [prev]

    for obs in range(Observation.shape[0] - 2, -1, -1):
        prev = int(major[prev, obs])
        ship.append(prev)
    return ship[::-1], solved[:, -1].max()
