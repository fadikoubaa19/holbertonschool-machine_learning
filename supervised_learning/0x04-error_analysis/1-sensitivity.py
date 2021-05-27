#!/usr/bin/env python3

import numpy as np


def sensitivity(confusion):
    """Calculates the sensitivity for each class in a confusion matrix"""
    a = confusion.sum(axis=0) - np.diag(confusion)
    b = confusion.sum(axis=1) - np.diag(confusion)
    c = np.diag(confusion)
    sm = confusion.sum() - (a + b + c)
    return c / (c + b)
