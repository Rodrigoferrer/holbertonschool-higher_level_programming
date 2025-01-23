#!/usr/bin/python3
def multiple_returns(sentence):
    slen = len(sentence)
    if slen <= 0:
        return slen, None
    return slen, sentence[0]
