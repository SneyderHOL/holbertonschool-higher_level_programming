#!/usr/bin/python3
def print_square(size):
    """print_square is a function that prints a square with the character #
    Args:
        size (int): size of the square to print

    Raises:
        TypeError: if size is not an integer or if size is a float and is less
        than 0
        ValueError: if size is less than 0
    """
    if type(size) != int:
        if (type(size) == float and size < 0) or type(size) != float:
            raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    if size > 0:
        for x in range(size):
            for i in range(size):
                print('#', end="")
            print('')
    else:
        print('', end='')
