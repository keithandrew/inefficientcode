def uniques_only(iterator):
    unique_set = []
    unique_test = set()

    for item in iterator:
        if item not in unique_test:
            unique_set.append(item)
            unique_test.add(item)

    return unique_set
