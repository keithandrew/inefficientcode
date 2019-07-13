def get_earliest(*args):
    """Takes in an arbitrary number of datestrings in american
    format (mm/dd/yyyy) and returns the earliest"""

    date_list = []
    lowest = ""
    tie = "There is a tie between:\n"

    for x in args:
        date_list.append(x.split("/"))
    levels = [list(j) for j in zip(*date_list)]

    while not lowest:
        if len(set(levels[2])) != 1:
            for a, b in reversed(list(enumerate(levels[2]))):
                low = min(levels[2])
                if int(b) > int(low):
                    levels[2].pop(a)
                    levels[1].pop(a)
                    levels[0].pop(a)
            if len(levels[2]) == 1:
                for x in args:
                    if levels[2][0] in x:
                        lowest += str(x)
            print(levels[2])

        if len(set(levels[0])) != 1:
            for c, d in reversed(list(enumerate(levels[0]))):
                low = min(levels[0])
                if int(d) > int(low):
                    levels[2].pop(c)
                    levels[1].pop(c)
                    levels[0].pop(c)
            if len(levels[0]) == 1:
                for x in args:
                    if levels[0][0] in x:
                        lowest += str(x)
            print(levels[0])

        if len(set(levels[1])) != 1:
            for e, f in reversed(list(enumerate(levels[1]))):
                low = min(levels[1])
                if int(f) > int(low):
                    levels[2].pop(e)
                    levels[1].pop(e)
                    levels[0].pop(e)
            if len(levels[1]) == 1:
                for x in args:
                    if levels[1][0] in x:
                        lowest += str(x)
            print(levels[1])
    return lowest
