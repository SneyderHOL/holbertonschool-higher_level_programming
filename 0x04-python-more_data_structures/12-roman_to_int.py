#!/usr/bin/python3
def roman_to_int(roman_string):
    dictionary = roman_dictionary()
    num, sub = 0, 0
    if roman_string.isalpha():
        for c in roman_string:
            if c in dictionary:
                if ((sub == 1 and dictionary[c] == 10) or
                        (sub == 1 and dictionary[c] == 5)):
                    num += dictionary[c] - 2
                else:
                    num += dictionary[c]
                sub = dictionary[c]
            else:
                num = 0
                break
    return num


def roman_dictionary():
    dictionary = ({'I': 1, 'V': 5, 'X': 10, 'L': 50,
                   'C': 100, 'D': 500, 'M': 1000})
    return dictionary
