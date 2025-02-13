# Program is a simple game of hangman.
# Program takes a word from a list and prints how many letter it has.
# Player guesses which letter is in the word.
# If Player guesses correctly program prints where the letter is.
# If Player guesses incorrectly program takes one life from the pool, and prints another stage of hangman drawing.
# Player wins if he guesses whole word before whole hangman is printed (6 lives)

import random
import hangman_picture
from hangman_words import word_list
from hangman_logo import logo
def guess():
    while True:
        try:
            a = str(input("Enter a letter: ")).lower()
            if len(a) == 1 and a.isalpha():
                return a
            else:
                print("It is not a valid input, try agin")
        except ValueError:
            print("It is not a valid input, try agin")


def game():
    word_original = list(random.choice(word_list))
    word=[]
    wrong_guesses = []
    live=6
    for i in range(len(word_original)):
        word.append("_")
    print(' '.join(word))

    while "_" in word and live>0:
        if live < 6:
            print(f"You hav tried {wrong_guesses}")
        letter = guess()
        if letter in word_original:
            for i in range(len(word_original)):
                if word_original[i] == letter:
                    word[i]=letter
            print(' '.join(word))
        elif letter in wrong_guesses:
            print("You hav already tried this letter")
        else:
            live -=1
            print(f"Wrong letter, you have {live}/6 lives remaining")
            if live>0:
                wrong_guesses.append(letter)
                hangman_picture.pictures(live)
                print(' '.join(word))
    if live>0:
        print ("******Congratulation you have wan the game!******")
    else:
        hangman_picture.pictures(live)
        print(f"******You have lost the game****** correct world was: {''.join(word_original)}")

print(logo)
print("We are going to play a hangman!\nYou have to guess letters in order to guess the word, before your lives runs out")
play=1
while play == 1:
    game()
    play=int(input("If you would like to play agin enter 1: "))
