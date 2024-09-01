#!/usr/bin/python3
"""The island permiter problem."""


def island_perimeter(grid):
    """Island permiter problem."""
    prem = 0
    rootIndex = 0
    for x in grid:
        index = 0
        for xx in x:
            if xx:
                n = 4
                try:
                    # is there a 1 next ?
                    if grid[rootIndex][index + 1] == 1:
                        n -= 1
                except Exception:
                    pass
                try:
                    # is there a 1 under ?
                    if grid[rootIndex + 1][index] == 1:
                        n -= 1
                except Exception:
                    pass
                # is there a 1 before ?
                if index - 1 >= 0 and grid[rootIndex][index - 1] == 1:
                    n -= 1
                # is there a 1 above?
                if rootIndex - 1 >= 0 and grid[rootIndex - 1][index] == 1:
                    n -= 1
                if n > 0:
                    prem += n
                # print(f"Found land, at {rootIndex} at {index} with p {n}")
            index += 1

        rootIndex += 1
    return prem
