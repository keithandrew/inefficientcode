def uniques_only(iterator):
    uniques = []

    for item in iterator:
        if item not in uniques:
            uniques.append(item)

    print(uniques)


hashables = [(n, n + 1) for n in range(1000)] + [0]
unhashables = [[n] for n in range(1000)] + [0]
uniques_only(unhashables)
