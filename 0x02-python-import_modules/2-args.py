#!/bin/usr/python3
if __name__ == "__main__":
    from sys import argv
    c = len(argv) - 1

    if c == 0:
        print("0 arguments.")
    elif c == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(c))
    for num in range(c):
        print("{}: {}".format(num + 1, argv[num + 1])

