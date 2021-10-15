#!/usr/bin/env python3
""" 0-markov_chain.py """


import numpy as np


def markov_chain(P, s, t=1):
    """
    function markov_chain
    param: p, s ,t
    """

    # if p is squar 2D return none
    if type(P) != np.ndarray:
        return None
    if type(t) is not int or t < 0:
        return None
    #represent the prob
    for j in range(0, t):
        s = np.matmul(s, P)
    return s
