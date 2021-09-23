#!/usr/bin/env python3
"""
Create 4-positional_encoding
"""
import numpy as np


def positional_encoding(max_seq_len, dm):
    """
    function positional_encoding
    param --> max_seq_len /// ----> dm
    """
    out_put = np.zeros((max_seq_len, dm))

    for a in range(max_seq_len):
        for b in range(0, dm, 2):
            div_term = np.exp(b * -np.log(10000.0) / dm)
            out_put[a, b] = np.sin(a * div_term)
            out_put[a, b + 1] = np.cos(a * div_term)

    # Return out_put
    return out_put
