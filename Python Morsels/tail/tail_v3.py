def tail(sequence, n):
    """
    Takes an input sequence and return last n elements

    Sequence: List, Tuple, String, Set
    n: positive integer
    """

    tail = []  # define element storage

    if n <= 0:  # return empty list if n < 0
        return tail

    for element in sequence:  # iterate through input
        tail.append(element)  # append to storage
        if len(tail) > n:  # reduce memory consumption by discarding if list > n
            tail.pop(0)
    return tail  # return result
