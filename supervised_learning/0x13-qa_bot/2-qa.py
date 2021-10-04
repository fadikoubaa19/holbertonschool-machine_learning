#!/usr/bin/env python3
"""
Function that answers from references
"""

question_answer = __import__('0-qa').question_answer


def answer_loop(reference):
    """
    answer from refrences
    """
    while True:
        text = input("Q: ")
        if text in ["exit", "quit", "goodbye", "bye"]:
            print("A: Goodbye")
            break
        answer = question_answer(text, reference)

        # If answer caanot be found respond Message
        if answer is None or answer == '':
            print('A: Sorry, I do not understand your question.')
        else:
            print('A: {}'.format(answer))
