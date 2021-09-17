#!/usr/bin/env python3
"""Calculates the unigram BLEU score"""
import numpy as np


def uni_bleu(references, sentence):
    """
    References ==> is a list of refences transaltions.
    Sentences ===> is a list containing the model proposed sentence.
    Return the unigram BLEU score.
    """

    S1 = list(set(sentence))
    LW = {}

    for reference in references:
        for key in reference:
            if key in S1:
                if key not in LW.keys():
                    LW[key] = reference.count(key)
                else:
                    up = reference.count(key)
                    Last = LW[key]
                    LW[key] = max(up, Last)

    pple = len(sentence)
    solv = sum(LW.values()) / pple

    List = []
    for reference in references:
        len_ref = len(reference)
        difference = abs(len_ref - pple)
        List.append((difference, len_ref))

    sorts = sorted(List, key=lambda x: x[0])

    cap = sorts[0][1]

    if pple > cap:
        id = 1
    else:
        id = np.exp(1 - (cap / pple))

    Result = id * np.exp(np.log(solv))
    return Result
