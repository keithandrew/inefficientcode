"""
Number Names - Show how to spell out a number in English. You can use a \
preexisting implementation or roll your own, but you should support inputs \
up to at least one million (or the maximum value of your language's default \
bounded integer type, if that's less). Optional: Support for inputs other \
than positive integers (like zero, negative integers, and floating-point numbers).
"""

# set up the necessary dictionaries
number_dict = {
    "single": {
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
    },
    "teens": {
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
    },
    "compound": {
        2: "Twenty",
        3: "Thirty",
        4: "Forty",
        5: "Fifty",
        6: "Sixty",
        7: "Seventy",
        8: "Eighty",
        9: "Ninety",
    },
}


def number_names(input_number):
    """Takes in a number are returns it in word form as a string"""

    # set up conversion and storage structures
    num = str(input_number)
    magnitude = len(num)

    if magnitude == 1:
        return f"{number_dict['single'][int(num)]}"
    if magnitude == 2:
        return f"{check_tens(num)}"
    if magnitude == 3:
        x, y = check_hundreds(num)
        return f"{x}{y}"
    if magnitude == 4:
        x, y = check_hundreds(num[1:])
        return f"{number_dict['single'][int(num[0])]} Thousand {x}{y}"
    if magnitude == 5:
        x = check_tens(num[:2])
        y, z = check_hundreds(num[2:])
        return f"{x} Thousand {y}{z}"
    if magnitude == 6:
        a, b = check_hundreds(num[:3])
        x, y = check_hundreds(num[3:])
        return f"{a}{b} Thousand {x}{y}"

    # for x, y in enumerate(num):
    #     working_dict.update({x: number_dict["single"][int(y)]})
    # print(working_dict)

    # determine length of number and apportion to keys


def check_tens(num_string):
    """Checks input and returns formatted string"""
    if int(num_string) != 0:

        if int(num_string) < 10:
            return number_dict["single"][int(num_string)]
        elif int(num_string) < 20:
            return number_dict["teens"][int(num_string)]
        elif int(num_string[1]) == 0:
            return number_dict["compound"][int(num_string[0])]
        else:
            return (
                number_dict["compound"][int(num_string[0])]
                + "-"
                + number_dict["single"][int(num_string[1])]
            )

    else:
        return ""


def check_hundreds(num_string):
    """checks input and returns formatted string"""
    if int(num_string) != 0:
        tens = check_tens(num_string[1:])

        if int(num_string) < 100:
            return "", "and " + tens
        elif tens:
            return (number_dict["single"][int(num_string[0])] + " Hundred and ", tens)
        else:
            return number_dict["single"][int(num_string[0])] + " Hundred", tens

    else:
        return "", ""


print(number_names(123456))
