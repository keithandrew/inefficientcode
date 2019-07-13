def add(*matrices):
    row1 = []
    for a in zip(*matrices):
        for i in zip(*a):
            row1.append(sum([a for a in i]))
    return row1
