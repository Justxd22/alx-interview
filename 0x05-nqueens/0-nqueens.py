#!/usr/bin/python3
"""Nqueens Problem."""


import sys


def validate_input():
    """Validate the command-line input arguments."""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    if not sys.argv[1].isdigit():
        print("N must be a number")
        exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        exit(1)


def is_safe(row, col, queens):
    """Check if a queen can be placed at the given row and column."""
    for r, c in enumerate(queens):
        if c == col or abs(c - col) == abs(r - row):
            return False
    return True


def backtrack(row, queens, x, solutions):
    """Backtracking to solve."""
    if row == x:
        solutions.append([[r, c] for r, c in enumerate(queens)])
        return
    for col in range(x):
        if is_safe(row, col, queens):
            backtrack(row + 1, queens + [col], x, solutions)


def solve_n_queens(x):
    """Solve the N queens problem using backtracking."""
    solutions = []
    backtrack(0, [], x, solutions)
    return solutions


validate_input()
x = int(sys.argv[1])
solutions = solve_n_queens(x)
for solution in solutions:
    print(solution)
