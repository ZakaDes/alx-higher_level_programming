#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    cm = 0
    for i in range(x):
        try:
            print(my_list[i], end="")
            cm += 1
        except Exception as error:
            break
    print("")
    return (cm)
