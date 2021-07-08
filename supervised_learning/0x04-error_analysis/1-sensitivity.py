#!/usr/bin/env python3

import numpy as np


def sensitivity(confusion):
    """function that Calculates the sens"""

    a = np.sum(confusion, axis=1)
    a_positive = np.diagonal(confusion)
    result = a_positive / a

    return np.array(result)
