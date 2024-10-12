#!/usr/bin/python3

"""
Pascal's triangle
"""


def pascal_triangle(n):
    """  returns list of lists of integers representing
    the Pascal triangle of n """

    # the first row is always 1
    pyramid = [[1]]
    if n <= 0:
        return []
    # run through the remaining n rows
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(pyramid[i-1][j-1]+pyramid[i-1][j])
        row.append(1)
        pyramid.append(row)
    return pyramid
