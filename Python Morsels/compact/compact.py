# def compact(source_list):
#
#     compact_list = []
#
#     if not source_list:
#         return compact_list
#
#     compact_list.append(source_list[0])
#     for x, y in enumerate(source_list):
#         if x > 0 and source_list[x] != source_list[x - 1]:
#             compact_list.append(y)
#
#     return compact_list


# 2nd iteration of script
# def compact(source):
#
#     previous = None
#
#     for item in source:
#         if previous is None:
#             yield item
#             previous = item
#         else:
#             try:
#                 if item != previous:
#                     yield item
#                     previous = item
#             except TypeError:
#                 if item == previous:
#                     yield item
#                     previous = item

# 3rd iteration of script
# def compact(source):
#
#     previous = None
#
#     for item in source:
#         if previous is None:
#             yield item
#             previous = item
#         elif item != previous:
#             yield item
#             previous = item
#         elif item == previous:
#             yield item
#             previous = item

# 4th iteration of script
# def compact(source):
#
#     previous = None
#
#     for item in source:
#         if previous is None:
#             yield item
#             previous = item
#         elif item != previous:
#             yield item
#             previous = item
#         previous = item

# final iteration of script
def compact(source):

    previous = None  # keep track of previous element

    for item in source:  # iterate through ioterable
        if previous is None or item != previous:  # if element is alone
            yield item  # yield and move to next element
            previous = item  # update previous value to next value

        previous = item  # do nothing if adjacent is duplicate, update previous value
