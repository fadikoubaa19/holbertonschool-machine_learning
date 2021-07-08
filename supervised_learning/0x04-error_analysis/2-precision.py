#!/usr/bin/env python3
"""Error Analysis module"""
import numpy as np


def precision(confusion):
    """Calculates the precision for each class in a confusion matrix
    """
    CL = confusion.sum(axis=0) - np.diag(confusion)
    CA = confusion.sum(axis=1) - np.diag(confusion)
    CM = np.diag(confusion)
    TN = confusion.sum() - (CL + CA + CM)
    return CM / (CM + CL)
