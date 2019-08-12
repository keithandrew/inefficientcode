def tail(input_sequence, n):
    """
    Takes an input sequence and return last n elements

    Sequence: List, Tuple, String, Set
    n: positive integer
    """

    sequence = []  # define element storage

    if n <= 0:  # return empty list if n < 0
        return sequence

    for element in input_sequence:  # iterate through input
        sequence.append(element)  # append to storage
        if len(sequence) > n:  # reduce memory consumption by discarding if list > n
            sequence.pop(0)
    return sequence  # return result


squares = (n ** 2 for n in range(10))
print(tail(squares, 3))
