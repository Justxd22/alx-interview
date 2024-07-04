#!/usr/bin/python3
"""Lockboxes interview question."""


def canUnlockAll(boxes):
    """Lockboxes problem."""
    opened = [False] * len(boxes)
    opened[0] = True
    run = 2

    while run:
        for i in range(len(boxes)):
            if not opened[i]:
                continue
            keys = boxes[i]
            for x in keys:
                if x < len(boxes):
                    opened[x] = True
        run -= 1

    return all(opened)
