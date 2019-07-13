def get_earliest(a, b):
    alist = [a.split("/"), b.split("/")]
    lowest = ""

    levels = [(i, j) for i, j in zip(alist[0], alist[1])]

    if levels[2][0] < levels[2][1]:
        lowest += a
    elif levels[2][0] > levels[2][1]:
        lowest += b
    elif levels[0][0] < levels[0][1]:
        lowest += a
    elif levels[0][0] > levels[0][1]:
        lowest += b
    elif levels[1][0] < levels[1][1]:
        lowest += a
    elif levels[1][0] > levels[1][1]:
        lowest += b
    else:
        print(f"{a} & {b} are equal")
    return lowest
