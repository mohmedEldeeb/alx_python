#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    item = []
    for line in matrix:
        line_list = map(lambda num: num * num, line)
        item.append(list(line_list))
    return (item)

