#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        best = (0, 0)
        for k, v in a_dictionary.items():
            if best[1] < v:
                best = (k, v)
        return best[0]
