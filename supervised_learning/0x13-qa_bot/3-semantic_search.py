#!/usr/bin/env python3
"""Create function that performs semantic search """


import numpy as np
import os
import tensorflow_hub as hub


def semantic_search(corpus_path, sentence):
    """ function semantic_search"""

    document = [sentence]

    for i in os.listdir(corpus_path):
        if not i.endswith('.md'):
            continue
        with open(corpus_path + '/' + i, 'r', encoding='utf-8') as file:
            document.append(file.read())
    #Load the link.
    link = hub.load(
        'https://tfhub.dev/google/universal-sentence-encoder-large/5')

    #embedding the link of doc
    embeddings = link(document)
    
    
    # returns the sum product 
    sl = np.inner(embeddings, embeddings)
    
    # Returns the indices of the maximum values along an axis
    ex = np.argmax(sl[0, 1:])

    return document[ex + 1]
