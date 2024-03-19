#!/usr/bin/python3
def no_c(my_string):
    res = ''
    for count in my_string:
        if count != 'c' and count != 'C':
            res += count
    return (res)
