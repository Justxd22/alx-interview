#!/usr/bin/python3
"""Lockboxes interview question."""


def canUnlockAll(boxes):
    """Lockboxes problem."""
    keys = []
    opened = [False] * len(boxes)
    run = 2

    while run:
        opened[0] = True
        for i in range(len(boxes)):
            if not opened[i]:
                continue
            keys = boxes[i]
            for x in keys:
                opened[x] = True
        run -= 1

    return all(opened)
