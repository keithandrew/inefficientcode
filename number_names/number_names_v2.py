"""
Number Names - Show how to spell out a number in English. You can use a \
preexisting implementation or roll your own, but you should support inputs \
up to at least one million (or the maximum value of your language's default \
bounded integer type, if that's less). Optional: Support for inputs other \
than positive integers (like zero, negative integers, and floating-point numbers).
"""


def number_names(num):
    """Takes in a number are returns it in word form as a string"""

    # set up the necessary dictionaries
    number_dict = {
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

    double_dict = {
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

    # set up conversion and storage structures

    working_num = str(num)
    units_key = ""
    tens_key = ""
    hundreds_key = ""
    th_key = ""
    tth_key = ""
    hth_key = ""

    # determine length of number and apportion to keys

    magnitude = len(working_num)

    if num < 10:
        return number_dict[num]
    if 9 < num < 20:
        return double_dict[num]
    if 19 < num < 100:
        units_key = number_dict[int(working_num[1])]
        tens_key = compound_dict[int(working_num[0])]
        return f'{tens_key}-{units_key}'
    if magnitude == 3:
        units_key = number_dict[int(working_num[2])]
        tens_key = compound_dict[int(working_num[1])]
        hundreds_key = number_dict[int(working_num[0])]
        return f"{hundreds_key} Hundred and {tens_key}-{units_key}"
    if magnitude == 4:
        units_key = number_dict[int(working_num[3])]
        tens_key = compound_dict[int(working_num[2])]
        hundreds_key = number_dict[int(working_num[1])]
        th_key = number_dict[int(working_num[0])]
        return f"{th_key} Thousand, {hundreds_key} Hundred and {tens_key}-{units_key}"
    if magnitude == 5:
        units_key = number_dict[int(working_num[4])]
        tens_key = compound_dict[int(working_num[3])]
        hundreds_key = number_dict[int(working_num[2])]
        th_key = number_dict[int(working_num[1])]
        tth_key = compound_dict[int(working_num[0])]
        return f"{tth_key}-{th_key} Thousand, {hundreds_key} Hundred and {tens_key}-{units_key}"
    if magnitude == 6:
        units_key = number_dict[int(working_num[5])]
        tens_key = compound_dict[int(working_num[4])]
        hundreds_key = number_dict[int(working_num[3])]
        th_key = number_dict[int(working_num[2])]
        tth_key = compound_dict[int(working_num[1])]
        hth_key = compound_dict[int(working_num[0])]
        return f"{hth_key} Hundred and {tth_key}-{th_key} Thousand, {hundreds_key} Hundred and {tens_key}-{units_key}"
