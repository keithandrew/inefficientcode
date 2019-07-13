def add(*matrices):
    matrix_sum = []
    for a in zip(*matrices):
        row1 = []
        for i in zip(*a):
            row1.append(sum(i))
        matrix_sum.append(row1)
    return matrix_sum
