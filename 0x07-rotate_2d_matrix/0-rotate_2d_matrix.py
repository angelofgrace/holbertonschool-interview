#!/bin/python3
"""
rotate 2d matrix, 
TODO strike that, reverse it
"""

def rotate_2d_matrix(matrix):
    # Iterate through squares one by one
    N = len(matrix)
    for x in range(0, int(len(matrix)/2)):
        for y in range(x, len(matrix)-x-1):
            # store current cell in temp variable
            temp = matrix[x][y]
 
            # move values from right to top
            matrix[x][y] = matrix[y][N-1-x]
 
            # move values from bottom to right
            matrix[y][N-1-x] = matrix[N-1-x][N-1-y]
 
            # move values from left to bottom
            matrix[N-1-x][N-1-y] = matrix[N-1-y][x]
 
            # assign temp to left
            matrix[N-1-y][x] = temp
