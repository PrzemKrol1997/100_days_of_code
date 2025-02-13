student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#TODO 1. Create a dictionary in this format:
file = pandas.read_csv("nato_phonetic_alphabet.csv")
dictionary = {row.letter:row.code for (index, row) in file.iterrows()}



#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter word: ").upper()
list_of_codes = [dictionary[name_letter] for name_letter in word]
print(list_of_codes)
