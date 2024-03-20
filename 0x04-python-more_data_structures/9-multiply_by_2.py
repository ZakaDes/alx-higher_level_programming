#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    n_dict = a_dictionary.copy()
    for i in n_dict.keys():
        n_dict[i] = n_dict[i] * 2
    return (n_dict)
