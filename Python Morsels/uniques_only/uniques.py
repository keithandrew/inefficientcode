def uniques_only(iterator):
    unique_set = set()

    while True:
        for num in iterator:
            unique_set.add(num)

        return iter(unique_set)
