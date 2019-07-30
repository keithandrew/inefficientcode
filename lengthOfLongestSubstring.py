# def lengthOfLongestSubstring(self, s: str) -> int:
#
#         string_dict = dict()
#         string = ""
#         n = 0
#
#         for letter in s:
#             if letter in string:
#                 string_dict[n] = len(string)
#                 n += 1
#                 string = letter
#             else:
#                 string += letter
#
#         string_dict[n] = len(string)
#
#         return max(string_dict.values())

# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#
#         string_dict = dict()
#         string = ""
#         n = 0
#
#         for letter in s:
#             if letter in string:
#                 string_dict[n] = len(string)
#                 string += letter
#                 string = string[1::]
#                 n += 1
#             else:
#                 string += letter
#
#         string_dict[n] = len(string)
#
#         return max(string_dict.values())


# def lengthOfLongestSubstring(s):
#     string_dict = dict()
#     string = ""
#     n = 0
#
#     for letter in s:
#         if letter in string:
#             string_dict[n] = len(string)
#             string += letter
#             string = string[1::]
#             n += 1
#         else:
#             string += letter
#             string_dict[n] = len(string)
#         print(string)
#
#     return max(string_dict.values())
#
#
# print(lengthOfLongestSubstring("pwwkew"))

# def lengthOfLongestSubstring(self, s: str) -> int:
#
#         string_dict = dict()
#         string = ""
#         n = 0
#         start = 1
#
#         for letter1 in s:
#             string = letter1
#             for letter2 in s[start:]:
#                 if letter2 in string:
#                     n += 1
#                     start += 1
#                     break
#                 else:
#                     string += letter2
#                     string_dict[n] = len(string)
#
#         return max(string_dict.values())

# def lengthOfLongestSubstring(self, s: str) -> int:
#
#         string_dict = dict(default=1)
#         string = ""
#         n = 0
#         start = 1
#
#         for letter1 in s:
#             string = letter1
#             for letter2 in s[start:]:
#                 if letter2 in string:
#                     n += 1
#                     start += 1
#                     break
#                 else:
#                     string += letter2
#                     string_dict[n] = len(string)
#
#         return max(string_dict.values())


def lengthOfLongestSubstring(s):
    """first correct answer"""

    string_dict = dict(default=1)
    string = ""
    n = 0
    start = 1

    if s == 0:
        return 0

    for letter1 in s:
        string = letter1
        for letter2 in s[start:]:
            if letter2 in string:
                n += 1
                start += 1
                break
            else:
                string += letter2
                string_dict[n] = len(string)

    return max(string_dict.values())


print(lengthOfLongestSubstring("au"))
