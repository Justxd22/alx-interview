#!/usr/bin/python3
"""Prime game problem."""

def sieve_of_eratosthenes(max_n):
    """Use the Sieve of Eratosthenes to precompute primes up to max_n."""
    is_prime = [True] * (max_n + 1)
    is_prime[0] = is_prime[1] = False

    p = 2
    while p * p <= max_n:
        if is_prime[p]:
            for i in range(p * p, max_n + 1, p):
                is_prime[i] = False
        p += 1
    return is_prime


def calculate_prime_wins(max_n, is_prime):
    """Calculate the number of wins for prime picking up to max_n."""
    wins = [0] * (max_n + 1)

    for n in range(1, max_n + 1):
        prime_count = 0

        for i in range(1, n + 1):
            if is_prime[i]:
                prime_count += 1

        if prime_count % 2 == 1:
            wins[n] = "Maria"
        else:
            wins[n] = "Ben"

    return wins


def isWinner(x, nums):
    """Determine the overall winner between Maria and Ben."""
    if not nums or x <= 0:
        return None

    max_n = max(nums)
    is_prime = sieve_of_eratosthenes(max_n)
    wins = calculate_prime_wins(max_n, is_prime)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if wins[n] == "Maria":
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
