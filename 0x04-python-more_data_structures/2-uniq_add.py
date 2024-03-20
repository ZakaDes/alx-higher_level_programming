#!/usr/bin/python3
def uniq_add(my_list=[]):
    lis = set(my_list)
    sum = 0
    for i in lis:
        sum = sum + i
    return sum
