#!/usr/bin/env python3
""" task 4"""


from gensim.models import FastText


def fasttext_model(sentences, size=100, min_count=5, negative=5,
                   window=5, cbow=True, iterations=5, seed=0, workers=1):
    """
    ___________________________________________________
    |*Sentences ==> is a list of_______________________|
    |sentences to be trained on._______________________|_____
    |*size ==> is the demtionansily_________________________|
    |of the embdedding layer._______________________________|
    |*min_count ==> is the minimum number of________________|
    | occurences of a word for use training.________________|
    |*window ==> is the maximum distance between the current|
    |and predicted word withing a sentences.________________|
    |negative ==> is the size of negative sampling_________|
    |cbow is boolean to determine the training type________|
    |TRUE is for CBOW: False is for skip-gam.______________|
    -------------------------------------------------------
    """
    # model Elements
    model = FastText(sentences,
                     size=size,
                     min_count=min_count,
                     window=window,
                     negative=negative,
                     sg=cbow,
                     seed=seed,
                     workers=workers)
    # Train model + Return the trained model
    model.train(sentences,
                total_examples=model.corpus_count,
                epochs=iterations)

    return model
