#!/usr/bin/python3
"""Rotate 2d matrix."""


def rotate_2d_matrix(mat):
    """Rotate 2d matrix."""
    x = len(mat)
    for xx in range(x):
        for xxx in range(xx, x):
            mat[xx][xxx], mat[xxx][xx] = mat[xxx][xx], mat[xx][xxx]

    for xx in range(x):
        mat[xx].reverse()
