def uniques_only(iterator):
    uniques = []

    for item in iterator:
        if item not in uniques:
            uniques.append(item)

    return iter(uniques)
