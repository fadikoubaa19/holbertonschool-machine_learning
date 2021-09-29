#!/usr/bin/env python3
"""0-dataset.py"""
import tensorflow.compat.v2 as tf
import tensorflow_datasets as tfds

tf.compat.v1.enable_eager_execution()


class Dataset:
    """loads and preps a dataset for machine translation"""
    def __init__(self):
        """---Function init---
        param: ---> self"""
        lorum, metadata = tfds.load('ted_hrlr_translate/pt_to_en',
                                       with_info=True,
                                       as_supervised=True)
        self.data_train, self.data_valid = lorum['train'], \
            lorum['validation']

        self.tokenizer_pt, self.tokenizer_en = self.tokenize_dataset(
            self.data_train)

    def tokenize_dataset(self, data):
        """
        Function tokenize_dataset
        param: ---> self // ---> data
        """
        tokenizer_pt = tfds.features.text.SubwordTextEncoder.build_from_corpus(
            (pt.numpy() for pt, en in data), target_vocab_size=2 ** 15)
        tokenizer_en = tfds.features.text.SubwordTextEncoder.build_from_corpus(
            (en.numpy() for pt, en in data), target_vocab_size=2 ** 15)
        return tokenizer_pt, tokenizer_en
