def is_anagram(string1, string2):
    comp_1 = sorted(string1.replace(" ", "").lower())
    comp_2 = sorted(string2.replace(" ", "").lower())
    return comp_1 == comp_2


is_anagram("Coins kept", "in pockets")
