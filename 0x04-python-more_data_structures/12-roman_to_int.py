#!/usr/bin/python3
def roman_to_int(roman_string):
    dic = roman_dictionary()
    word = roman_string
    num = 0
    if word.isalpha():
        for i in range(len(word)):
            if exist_in_dictionary(dic, word[i]):
                if i != len(word) - 1:
                    if dic[word[i]] >= dic[word[i + 1]]:
                        num += dic[word[i]]
                    else:
                        num -= dic[word[i]]
                else:
                    num += dic[word[i]]
            else:
                num = 0
                break
    return num


def roman_dictionary():
    dictionary = ({'I': 1, 'V': 5, 'X': 10, 'L': 50,
                   'C': 100, 'D': 500, 'M': 1000})
    return dictionary


def exist_in_dictionary(dictionary, value):
    return value in dictionary
