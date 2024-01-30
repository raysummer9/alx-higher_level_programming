#!/usr/bin/python3


""" Defination of text-indentation function."""

def text_indentation(text):
    """
    Prints texts

    args:
        text(str)
        no space at the begining of the line.
    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    for delim in ".:?":
        text = (delim + "\n\n").join(
                [line.strip(" ") for line in text.split(delim)])

    print(f"{text}", end="")
