def uniques_only(iterable):
    uniques_list = []
    seen_set = set()

    for item in iterable:
        try:
            if item not in seen_set:
                yield item
                seen_set.add(item)
        except TypeError:
            if item not in uniques_list:
                yield item
                uniques_list.append(item)
