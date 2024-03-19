#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    nlist = []
    for m in my_list:
        if m % 2 == 0:
            nlist.append(True)
        else:
            nlist.append(False)
    return (nlist)
