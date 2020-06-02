#!/usr/bin/python3
"""  Module for class MyList  """


class MyList(list):
    """  MyList Class """
    def print_sorted(self):
        """print_sorted: method that prints the list, but sorted
            (ascending sort)
        """
        print(sorted(self))
