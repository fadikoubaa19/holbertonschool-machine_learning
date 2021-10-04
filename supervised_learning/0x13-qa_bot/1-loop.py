#!/usr/bin/env python3
"""
Create a script that takes in input from the user with the prompt
"""
while True:
    text = input("Q: ")

    # print Goodbye in case of exit
    if text in ["exit", "quit", "goodbye", "bye"]:
        print("A: Goodbye")
        break
    print("A:")
