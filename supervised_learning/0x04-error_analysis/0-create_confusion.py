#!/usr/bin/env python3

import numpy as np


def create_confusion_matrix(labels, logits):
    """creates a confusion matrix"""
    fml = np.zeros((labels.shape[1], labels.shape[1]))
    fml = np.dot(labels.T, logits)
    return fml
