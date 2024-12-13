#!/usr/bin/python3
""" 0x0A. Prime Game task 0. Prime Game """

def sieve_of_eratosthenes(n):
    """Returns a list of primes up to parameter value n, in ascending order.

    Args:
        n (int): upper bound on list of primes returned.

    Return:
        primes (list of int): list of primes <= n, or
        (None): on failure
    """
    if type(n) is not int or n < 2:
        return None

    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False  # 0 and 1 are not prime
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    primes = [x for x in range(2, n + 1) if sieve[x]]
    return primes


def isWinner(x, nums):
    """Simulates a game of primes between Ben and Maria, returns the winner.

    For each round of the game, players are given a set of consecutive integers
    starting from 1 up to and including n, and take turns choosing a prime
    number from the set and removing that number and its multiples from the
    set. The player that cannot make a move loses the game.

    Args:
        x (int): number of rounds
        nums (list of int): array of n values for each round of the game

    Return:
        (str): name of the player that won the most rounds, or
        (None): on failure or no winner found
    """
    if type(nums) is not list or not all(isinstance(n, int) for n in nums) or not all(n > 0 for n in nums):
        return None

    if type(x) is not int or x != len(nums):
        return None

    nums.sort()
    max_num = nums[-1]
    primes = sieve_of_eratosthenes(max_num)
    if primes is None:
        return None

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        prime_count = sum(1 for p in primes if p <= n)
        
        # The winner is determined by the number of primes
        if prime_count % 2 == 1:  # Odd number of primes -> Maria's turn
            maria_wins += 1
        else:  # Even number of primes -> Ben's turn
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
