"""Number Names - Takes an input integer and returns the number spelled out in english.
This implementation supports numbers up to 999,999, negative integers as well as
floating point number"""

# set up the conversion dictionary
number_dictionary = {
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


def number_names(numeric_value):
    """Takes in a number and returns it as a formatted text string"""

    input_number = str(numeric_value)  # convert input number to string to manipulate

    if "-" in input_number:  # check if number is negative
        if "." in input_number:  # check if number is integer or floating
            number = generate_float(input_number[1:])
            print("Negative " + number)
        else:
            number = generate_integer(input_number[1:])
            print("Negative " + number)

    else:  # if not negative...
        if "." in input_number:  # check if number is integer or floating
            number = generate_float(input_number)
            print(number)
        else:
            number = generate_integer(input_number)
            print(number)


def generate_float(number):
    """generates floating point numbers"""

    split_number = number.split(".")  # split the number on the decimal point
    whole_number = generate_integer(split_number[0])  # generate the integer part
    decimal = generate_fractional(split_number[1])  # generate the fractional part
    floating_number = whole_number + " Point " + decimal  # combine the two parts
    return floating_number


def generate_fractional(number):
    """generates the text formatted fractional part of a floating point number"""

    decimal = ""

    for n in number:  # loop through fractional string and concatenate to decimal string
        decimal += number_dictionary["single"][int(n)] + " "
    return decimal


def generate_integer(number):
    """generates the text formatted integer part"""

    digits = len(number)  # key to the pattern in the dictionary
    n = int()

    # slice and pass string patterns to generate_ functions to create text output
    if digits == 1:
        n = number_dictionary['single'][int(number)]
    if digits == 2:
        n = check_tens(number)
    if digits == 3:
        x, y = check_hundreds(number)
        n = x + y  # create string using tuple unpacking
    if digits == 4:
        x, y = check_hundreds(number[1:])  # process last 3 digits
        n = number_dictionary['single'][int(number[0])] + " Thousand " + x + y
    if digits == 5:
        x = check_tens(number[:2])  # process first 2 digits
        y, z = check_hundreds(number[2:])  # process last 3 digits
        n = x + " Thousand " + y + z  # create string using tuple unpacking
    if digits == 6:
        a, b = check_hundreds(number[:3])  # process first 3 digits
        x, y = check_hundreds(number[3:])  # process last 3 digits
        n = a + b + " Thousand " + x + y  # create string using tuple unpacking

    return n


def check_tens(number):
    """Checks input and returns formatted string"""

    if int(number) != 0:  # check if number is 0 and thus can be omitted

        if int(number) < 10:  # deals with inputs < 10
            tens = number_dictionary["single"][int(number)]
        elif int(number) < 20:  # deals with inputs in range 10:19
            tens = number_dictionary["teen"][int(number)]
        elif int(number[1]) == 0:  # deals with multiples of 10
            tens = number_dictionary["compound"][int(number[0])]
        else:  # deals with everything else
            tens = (
                number_dictionary["compound"][int(number[0])]
                + "-"
                + number_dictionary["single"][int(number[1])]
            )
    else:  # and omit if 0
        tens = ""  # by returning blank strings
    return tens


def check_hundreds(number):
    """checks input and returns formatted string tuple (hundred_thousands, hundreds)"""

    if int(number) != 0:  # check if multiple of 1000 and can thus be omitted
        tens = check_tens(number[1:])

        if int(number) < 100:  # if 0 is first digit in input e.g. 1,010
            t = "", "and " + tens
        elif tens:  # deals with 10s
            t = number_dictionary["single"][int(number[0])] + " Hundred and ", tens
        else:  # deals with multiples of 100
            t = number_dictionary["single"][int(number[0])] + " Hundred", tens

    else:  # and omit if 0
        t = "", ""  # by returning blank strings

    return t


number_names(-110500.762)
