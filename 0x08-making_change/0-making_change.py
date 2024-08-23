#!/usr/bin/python3
"""Changes comes from within."""


def makeChange(coins, total):
    """Calc change."""
    if total <= 0:
        return 0

    coins.sort(reverse=True)

    c = 0
    for coin in coins:
        if total >= coin:
            c += total // coin
            total %= coin

    return c if total == 0 else -1
