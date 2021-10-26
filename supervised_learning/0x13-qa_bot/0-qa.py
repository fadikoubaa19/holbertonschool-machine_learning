#!/usr/bin/env python3
"""
finds a snippet of text
"""
import tensorflow as tf
import tensorflow_hub as hub
from transformers import BertTokenizer

def question_answer(question, reference):
    """
    question answer
    """
    # Locking for encoding source utf8 by using tokenizer
    tokenizer = BertTokenizer.from_pretrained(
        'bert-large-uncased-whole-word-masking-finetuned-squad')

    # Load tf hub site by using hub.load
    model = hub.load("https://tfhub.dev/see--/bert-uncased-tf2-qa/1")

    # Providing a lexical scanner by using tokenize
    # Question is string contain the question to answer
    # Reference is string contain the reference of document

    question_tokens = tokenizer.tokenize(question)
    paragraph_tokens = tokenizer.tokenize(reference)

    # Cls & SEP are special token to deterlinate the ID
    tokens = ['[CLS]'] + question_tokens + ['[SEP]'] +\
        paragraph_tokens + ['[SEP]']

    # Return vocab as dict of token to index
    input_word_ids = tokenizer.convert_tokens_to_ids(tokens)
    input_mask = [1] * len(input_word_ids)
    input_type_ids = [0] * (1 + len(question_tokens) + 1) +\
        [1] * (len(paragraph_tokens) + 1)

    
    # Specifies the dimension index at which to expand the shape
    # By using tf.convert_to tensor the objects are transformed to tensor:
    input_word_ids, input_mask, input_type_ids = map(lambda t: tf.expand_dims(
        tf.convert_to_tensor(t, dtype=tf.int32), 0),
                             (input_word_ids, input_mask, input_type_ids))
    outputs = model([input_word_ids,
                    input_mask, input_type_ids])
    
    # Find the maximum value of short_start:
    # Find the maximum of value of short_end:
    short_start = tf.argmax(outputs[0][0][1:]) + 1
    short_end = tf.argmax(outputs[1][0][1:]) + 1
    
    # answer is the out of voccabulary:
    answer_tokens = tokens[short_start: short_end + 1]
    
    # Convert answer to strings:
    answer = tokenizer.convert_tokens_to_string(answer_tokens)
    
    # in case the answer is empty return none:
    if answer == "":
        return None
    
    # return the answer.
    return answer
