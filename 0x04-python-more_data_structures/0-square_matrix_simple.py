#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    n_mtx = []
    for i in matrix:
        n_mtx.append(list(map(lambda i: i**2, i)))
    return (n_mtx)
