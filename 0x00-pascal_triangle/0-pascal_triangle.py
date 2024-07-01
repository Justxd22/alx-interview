#!/usr/bin/python3
"""Func to calc the pascal triangle."""
def pascal_triangle(n):
    """Func to calc the pascal triangle."""
    pascal = []
    for x in range(n):
        r = [1] * (x+1)
        for k in range(1, x):
            r[k] = pascal[x-1][k-1] + pascal[x-1][k]
        pascal.append(r)

    return pascal
