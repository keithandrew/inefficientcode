"""
Number Names - Show how to spell out a number in English. You can use a \
preexisting implementation or roll your own, but you should support inputs \
up to at least one million (or the maximum value of your language's default \
bounded integer type, if that's less). Optional: Support for inputs other \
than positive integers (like zero, negative integers, and floating-point numbers).
"""


def number_names(num: int) -> str:
    """Takes in a number are returns it in word form as a string"""

    # set up the necessary dictionaries
    numbers = {
        0: "Zero",
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine",
    }

    teens = {
        10: "Ten",
        11: "Eleven",
        12: "Twelve",
        13: "Thirteen",
        14: "Fourteen",
        15: "Fifteen",
        16: "Sixteen",
        17: "Seventeen",
        18: "Eighteen",
        19: "Nineteen",
    }

    compound_dict = {
        2: "Twenty",
        3: "Thirty",
        4: "Forty",
        5: "Fifty",
        6: "Sixty",
        7: "Seventy",
        8: "Eighty",
        9: "Ninety",
    }

    num_strings = {1: "Hundred", 2: "Thousand"}

    # set up conversion and storage structures

    working_num = str(num)

    # determine length of number and apportion to keys

    magnitude = len(working_num)

    if num < 10:
        return numbers[num]
    if 9 < num < 20:
        return teens[num]
    if 19 < num < 100:
        return f"{compound_dict[int(working_num[0])]}-{numbers[int(working_num[1])]}"
    if magnitude == 3:
        return f"{numbers[int(working_num[0])]} Hundred and {compound_dict[int(working_num[1])]}-{numbers[int(working_num[2])]}"
    if magnitude == 4:
        return f"{numbers[int(working_num[0])]} Thousand, {numbers[int(working_num[1])]} Hundred and {compound_dict[int(working_num[2])]}-{numbers[int(working_num[3])]}"
    if magnitude == 5:
        if int(working_num[0:2]) < 20:
            return f"{teens[int(working_num[0:2])]} Thousand, {numbers[int(working_num[3])]} Hundred and {compound_dict[int(working_num[4])]}-{numbers[int(working_num[3])]}"
        else:
            return f"{compound_dict[int(working_num[0])]}-{numbers[int(working_num[1])]} Thousand, {numbers[int(working_num[2])]} Hundred and {compound_dict[int(working_num[3])]}-{numbers[int(working_num[4])]}"
    if magnitude == 6:
        return f"{numbers[int(working_num[0])]} Hundred and {compound_dict[int(working_num[1])]}-{numbers[int(working_num[2])]} Thousand, {numbers[int(working_num[3])]} Hundred and {compound_dict[int(working_num[4])]}-{numbers[int(working_num[5])]}"
