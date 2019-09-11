"""Number Names - Takes an input integer and returns the number spelled out in english.
This implementation supports numbers up to 999,999, negative integers as well as
floating point number"""

from decimal import Decimal
from math import log10
from typing import Union

# set up the vocabulary dictionary
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
    "teen": {
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


def number_names(numeric_value: Union[int, float]) -> str:
    """Returns a given integer value as a spelled out string representation"""

    if numeric_value < 0:  # check if number is negative
        if type(numeric_value) is float:  # check if number is integer or floating
            number = "Negative " + generate_float(abs(numeric_value))
        else:
            number = "Negative " + generate_integer(abs(numeric_value))

    else:  # if not negative...
        if type(numeric_value) is float:  # check if number is integer or floating
            number = generate_float(numeric_value)
        else:
            number = generate_integer(numeric_value)

    print(number)


def generate_float(numeric_value: float) -> str:
    """generates string representation of floating point numbers"""
    fractional = Decimal(str(numeric_value)) % 1
    whole = int(numeric_value)

    float = generate_integer(whole) + " Point " + generate_fractional(fractional)

    return float


def generate_fractional(fractional: Decimal) -> str:
    """generates the string representation of the fractional part of a float"""

    decimal = ""
    n = 1
    number = fractional * (10 ** (len(str(fractional)[2::])))

    while number >= n:  # uses mod operator to extract digits from integer value
        decimal = number_dict["single"][(number // n) % 10] + " " + decimal
        n *= 10

    return decimal


def generate_integer(number: int) -> str:
    """generates the string representation on an integer"""

    digits = int(log10(number) + 1)  # key to the pattern in the dictionary
    n = ""

    # slice and pass string patterns to generate_ functions to create text output
    if digits == 1:
        n = number_dict['single'][number]
    if digits == 2:
        n = gen_tens(number)
    if digits == 3:
        hundreds = gen_hundreds(number)
        n = hundreds
    if digits == 4:
        hundreds = gen_hundreds(number % 1000)  # process last 3 digits
        n = number_dict['single'][number // 1000] + " Thousand " + hundreds
    if digits == 5:
        thousands = gen_tens(number // 1000)  # process first 2 digits
        hundreds = gen_hundreds(number % 1000)  # process last 3 digits
        n = thousands + " Thousand " + hundreds
    if digits == 6:
        thousands = gen_hundreds(number // 1000)  # process first 3 digits
        hundreds = gen_hundreds(number % 1000)  # process last 3 digits
        n = thousands + " Thousand " + hundreds

    return n


def gen_tens(number: int) -> str:
    """generates string representation of 0's values"""

    if number != 0:  # check if number is 0 and thus can be omitted

        if number < 10:  # inputs < 10
            tens = number_dict["single"][number]
        elif number < 20:  # inputs in range 10:19
            tens = number_dict["teen"][number]
        elif int(number) % 10 == 0:  # multiples of 10
            tens = number_dict["compound"][number]
        else:  # deals with everything else
            tens = (
                number_dict["compound"][number // 10]
                + "-"
                + number_dict["single"][number % 10]
            )
    else:  # omit if 0
        return ""  # by returning blank strings

    return tens


def gen_hundreds(number: int) -> str:
    """generates string representation of 00's values"""

    if number != 0:  # check if multiple of 1000 and can thus be omitted
        tens = gen_tens(number % 100)

        if number < 100:  # if 0 is first digit in input e.g. 1,010
            t = "and " + tens
        elif tens:
            t = number_dict["single"][number // 100] + " Hundred and " + tens
        else:
            t = number_dict["single"][number / 100] + " Hundred"

    else:  # omit if 0
        t = ""  # by returning blank strings

    return t


number_names(10900)
