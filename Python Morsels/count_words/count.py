"""Python Morsels Problem 01/07/2019"""


def strip_punc(test_word):
    """takes in a word, tests for punctuation and returns cleaned word"""

    # set empty string to concatenate cleaned letters
    cleaned_word = ""

    # if no punctuation return word
    if all(i.isalnum() for i in test_word):
        cleaned_word = test_word
    else:
        # test if letter is first or last, then if alphanumeric
        for i in test_word:
            if (
                test_word.index(i) == 0
                or test_word.index(i) == len(test_word) - 1
            ) and not i.isalnum():
                continue
            else:
                # concatenate letter if clean
                cleaned_word += i

    return cleaned_word


def count_words(string):
    """Takes in a string, and indexes it based on frequency of usage"""

    # define storage dictionary and word list, forcing words to lower case
    index_dict = {}

    # interate through the list and update dictionary values
    for word in string.lower().split():
        clean_word = strip_punc(word)

        if clean_word in index_dict:
            index_dict[clean_word] += 1
        else:
            index_dict.update({clean_word: 1})

    return index_dict
