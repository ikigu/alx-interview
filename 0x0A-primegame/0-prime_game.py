#!/usr/bin/python3

"""Contains isWinner function"""


def is_prime(n):
    """
    Determines whether a number is a prime number

    Args:
        n (int): Number to test

    Returns:
        True if number is prime, False otherwise
    """
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def get_primes(end):
    """
    Generates a list of prime numbers from 1 to current n
    """
    primes = [n for n in range(1, end + 1) if is_prime(n)]
    return primes


def isWinner3(x, nums):
    """
    Determines the winner of the prime game

    Args:
        x (int): number of rounds played
        nums (list): list of ints that represents n for each round
    """

    if not x or type(x) is not int:
        return None

    if type(nums) is not list:
        return None

    if x == 0:
        return None

    maria_win_count = 0
    ben_win_count = 0

    for num in nums:
        round = list(range(1, num + 1))
        prime_numbers_in_set = get_primes(num)

        if not prime_numbers_in_set:
            ben_win_count += 1
            break

        marias_turn = True

        while (True):
            if not prime_numbers_in_set:
                if marias_turn:
                    ben_win_count += 1
                else:
                    maria_win_count += 1
                break

            smallest_prime = prime_numbers_in_set.pop(0)
            round.remove(smallest_prime)

            round = [x for x in round if x % smallest_prime != 0]

            marias_turn = not marias_turn

    if maria_win_count > ben_win_count:
        return "Maria"

    if maria_win_count < ben_win_count:
        return "Ben"

    return None

# Algorithm
    # Check the type of inputs, if not right return None
    # If x is 0 return None

    # Set the turn to be Maria's
    # Generate a list of prime numbers from num
    # If num == 1: return "Ben"
    # For each round:
    # Check whether the list of primes is greater than 0:
    # If it is 0, Ben wins that round
    # Player picks number at index 0
    # That number is removed from the list of primes
    # Check for multiples of that number throughout and remove them from list
    # Switch the turn


def isWinner2(x, nums):
    """
    Determines the winner of the prime game

    Args:
        x (int): number of rounds played
        nums (list): list of ints that represents n for each round
    """

    if not x or type(x) is not int:
        return None

    if type(nums) is not list:
        return None

    if x == 0:
        return None

    ben_win_count = 0
    maria_win_count = 0

    marias_turn = True

    for i in range(0, x):
        primes_list = get_primes(nums[i])
        numbers_in_round = list(range(1, nums[i] + 1))

        if len(primes_list) == 0:
            ben_win_count += 1
            continue

        while len(primes_list) > 0:
            smallest_prime = primes_list[0]
            primes_list.remove(smallest_prime)
            numbers_in_round.remove(smallest_prime)

            for number in numbers_in_round:
                if number % smallest_prime == 0:
                    primes_list.remove(number)
                    numbers_in_round.remove(number)

            marias_turn = not marias_turn

        if marias_turn:
            ben_win_count += 1
        else:
            maria_win_count += 1

    if maria_win_count > ben_win_count:
        return "Maria"

    if maria_win_count < ben_win_count:
        return "Ben"

    return None


def isWinner(x, nums):
    """
    Determines the winner of the prime game

    Args:
        x (int): number of rounds played
        nums (list): list of ints that represents n for each round
    """
    if not nums or x < 1:
        return None

    n = max(nums)
    primes = [True for _ in range(max(n + 1, 2))]

    for i in range(2, int(n**0.5) + 1):
        if not primes[i]:
            continue
        for j in range(i*i, n + 1, i):
            primes[j] = False

    primes[0] = primes[1] = False

    counter = 0

    for i in range(len(primes)):
        if primes[i]:
            counter += 1
        primes[i] = counter

    odds = 0

    for n in nums:
        odds += primes[n] % 2 == 1
    if odds * 2 == len(nums):
        return None
    if odds * 2 > len(nums):
        return "Maria"
    return "Ben"
