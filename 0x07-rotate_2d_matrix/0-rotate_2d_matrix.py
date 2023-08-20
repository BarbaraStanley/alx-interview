#!/usr/bin/python3
''' Script to rotate a given n x n 2D matrix 90 degrees clockwise '''


def rotate_2d_matrix(matrix):
    """
    rotate an n x n 2D matrix 90° clockwise
    args:   matrix: List[List[int]]
    return: None
    """
    N = len(matrix)

    for i in range(N):
        for j in range(i, N):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(N):
        matrix[i] = matrix[i][::-1]
