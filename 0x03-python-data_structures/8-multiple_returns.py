#!/usr/bin/python3
def multiple_returns(sentence):
    sen_len = len(sentence)
    if sen_len > 0:
        first_char = sentence[0]
    else:
        first_char = "None"
    return (sen_len, first_char)
