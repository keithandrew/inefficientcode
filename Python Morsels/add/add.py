def add(*matrices):

    matrix_sum = []
    if all(len(matrix) == len(matrices[0]) for matrix in matrices):
        for values in zip(*matrices):
            first = len(values[0])
            if all(len(lst) == first for lst in values):
                matrix_row = []
                matrix_row.append([sum(nums) for nums in zip(*values)])
                matrix_sum += matrix_row
            else:
                raise ValueError("Given matrices are not the same size")
    else:
        raise ValueError("Given matrices are not the same size")
    return matrix_sum


m1 = [[6, 6], [3, 1]]
m2 = [[1, 2], [3, 4], [5, 6]]
m3 = [[6, 6], [3, 1, 2]]
add(m1, m2)
