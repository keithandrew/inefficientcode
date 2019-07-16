def is_anagram(string1, string2):

    def clean_string(string):
        import unicodedata
        string = string
        cleaned_string = unicodedata.normalize('NFKD', string)
        return cleaned_string


    comp_1 = [letter for letter in clean_string(string1).lower() if letter.isalpha()]
    comp_2 = [letter for letter in clean_string(string2).lower() if letter.isalpha()]

    print(sorted(comp_1) == sorted(comp_2))


is_anagram("cardeografía", "radiográfica")
