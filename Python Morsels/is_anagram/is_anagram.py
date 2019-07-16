def is_anagram(string1, string2):
    comp_1 = [letter for letter in string1.lower() if letter.isalpha()]
    comp_2 = [letter for letter in string2.lower() if letter.isalpha()]

    print(sorted(comp_1) == sorted(comp_2))


is_anagram("a diet", "I'd eat")
