def tail(sequence, n):
    """
    Takes an input sequence and return last n elements

    Sequence: List, Tuple, String, Set
    n: positive integer
    """

    tail = []  # define element storage

    if n <= 0:  # return empty list if n < 0
        return tail
    else:
        tail = sequence[-n:]
        return tail


print(tail('hello', 0))
