#!/usr/bin/python3
"""
Test 0x07 - Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    n = len(matrix)  # size of the matrix (n x n)

    # Step 1: Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            # Swap element at (i, j) with (j, i)
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    # Step 2: Reverse each row
    for i in range(n):
        matrix[i].reverse()
