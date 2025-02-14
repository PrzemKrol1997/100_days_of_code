def enter_word():
    while True:
        try:
            word = input("Enter word: ").upper()
            return [dictionary[name_letter] for name_letter in word]
        except KeyError:
            print("Wrong input, try agin")

import pandas

file = pandas.read_csv("nato_phonetic_alphabet.csv")
dictionary = {row.letter:row.code for (index, row) in file.iterrows()}

list_of_codes = enter_word()
print(list_of_codes)
