#!/usr/bin/env python3
"""gensim to keras"""

from gensim.models import Word2Vec


def gensim_to_keras(model):
    """
    Function gensim_to_keras:
    param: model
    """
    return model.wv.get_keras_embedding(train_embeddings=True)
