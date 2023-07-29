#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if length == 0:
        return length, None
    elif length > 0:
        for x in sentence:
            return length, x

