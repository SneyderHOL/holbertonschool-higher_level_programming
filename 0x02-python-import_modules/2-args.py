#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    size = len(sys.argv) - 1
    arg = "argument"
    if size > 0:
        if size == 1:
            print("{} {}".format(size, arg + ":"))
        else:
            print("{} {}".format(size, arg + "s:"))
        for i in range(1, size + 1):
            print("{:d}: {}".format(i, sys.argv[i]))
    else:
        print("{} {}".format(size, arg + "s."))
