#!/usr/bin/env python3

""" contains word2vec_model function"""
from gensim.models import Word2Vec


def word2vec_model(sentences, size=100, min_count=5, window=5,
                   negative=5, cbow=True, iterations=5, seed=0, workers=1):
    """ Creates and trains gensim word2vec model"""
    modele = Word2Vec(sentences=sentences,
                      min_count=min_count,
                      iter=iterations,
                      size=size,
                      sg=cbow,
                      seed=seed,
                      negative=negative)
    modele.train(sentences=sentences,
                 total_examples=modele.corpus_count,
                 epochs=modele.epochs)
    return modele
