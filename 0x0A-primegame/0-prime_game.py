#!/usr/bin/python3
"""Prime game problem."""


def is_prime(x):
    """Check if a number is prime."""
    if x <= 1:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False

    # Only check for odd divisors up to √x
    for i in range(3, int(x ** 0.5) + 1, 2):
        if x % i == 0:
            return False

    return True


def pickWinner(pset):
    """Determine the winner by picking primes and removing their multiples."""
    roundx = 0
    while True:
        prime_found = False
        for x in pset:
            if is_prime(x):
                prime_found = True
                # Remove the prime and its multiples
                pset = [n for n in pset if n % x != 0]
                break

        if not prime_found:
            # No prime found; the last player who made a move wins
            # Maria(0) or Ben(1)
            return roundx % 2

        roundx += 1


def isWinner(x, nums):
    """Determine the overall winner between Maria and Ben."""
    maria = 0
    ben = 0

    for xx in range(x):
        root = nums[xx]
        pset = list(range(1, root + 1))
        winner = pickWinner(pset)
        if winner == 0:
            ben += 1
        else:
            maria += 1

    # Determine the winner based on the number of rounds won
    if maria > ben:
        return "Maria"
    elif ben > maria:
        return "Ben"
    else:
        return None
