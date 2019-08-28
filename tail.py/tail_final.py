from collections import deque


def tail(sequence, n):
    """
    Takes an input sequence and return last n elements

    Sequence: List, Tuple, String, Set
    n: positive integer
    """

    if n <= 0:  # return empty list if n < 0
        return []

    # use a fixed length (n) deque to iterate through sequence without committing
    # unneeded elements to memory, return as list
    return list(deque(sequence, n))
