#!/usr/bin/python3
"""
Module to generate Pascal's Triangle
"""

def pascal_triangle(n):
    '''
    Generates Pascal's Triangle with n rows.
    
    Args:
        n (int): Number of rows in the triangle.
    
    Returns:
        list of lists: Pascal's Triangle up to n rows.
    '''
    if n <= 0:
        return []
    
    triangle = []
    for i in range(n):
        if len(triangle) == 0:
            triangle.append([1])
        else:
            row = [1]
            # Generate inner elements of the row
            for j in range(1, len(triangle[-1])):
                row.append(triangle[-1][j] + triangle[-1][j - 1])
            row.append(1)
            triangle.append(row)
    
    return triangle

