#!/usr/bin/python3
def multiple_returns(sentence):
    slen = len(sentence)
    if slen <= 0:
        print("error")
    return slen, sentence[0]
