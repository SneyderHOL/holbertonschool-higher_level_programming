#!/usr/bin/python3
"""
Module that prints lines until a special character
"""


def text_indentation(text):
    """text_indentation is a function that prints a text with 2 new lines after
        each of these characters: '.', '?', and ':'
    Args:
        text (string): string to print

    Raises:
        TypeError: if text is not a string
    """
    if type(text) != str:
        raise TypeError('text must be a string')
    aux = ''
    for x in text:
        aux += x
        if x in ['.', '?', ':']:
            aux = aux.lstrip()
            aux = aux.rstrip()
            aux += '\n'
            print(aux)
            aux = ''
    if aux:
        aux = aux.lstrip()
        aux = aux.rstrip()
        print(aux, end='')
