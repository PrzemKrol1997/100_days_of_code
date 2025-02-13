# This is a simple guessing game. Computer generates a random number and player has to guess
# If player guesses to high or to low he is informed and loses a live if he guesses correctly he wins a game

from logo import logo

def enter_number():
    working_number = -1
    a=True
    while a:
        try:
            working_number = int(input("Enter number between 1 and 100: "))
            a = False
        except ValueError:
            print("wrong input try agin")
    return working_number


def game():
    print(logo)
    print("Welcome to the guessing game, where your goal is to gues the number computer is thinking")
    live = input('Do you want to play on "hard"(5 tries) or "easy"(10 tries)?: ').lower()
    if live == "hard":
        live = 4
    else:
        live = 9
    random_number = random.randint(1, 100)
    #print(random_number)
    number = enter_number()
    number_table = []
    while number != random_number and live>0:
        if 1 <= number <= 100:
            if number > random_number:
                print("Number to high")
                number_table.append(str(number)+" high")
            else:
                 print("Number to low")
                 number_table.append(str(number)+" low")
            print(f"you have {live} remaining")
            print ("You have tried:", number_table)
            number =enter_number()
            live -= 1
        else:
            print("wrong input try agin")
    if live>0:
        print(f"\n******Congratulation, you guest the correct number: {random_number}******")
    else:
            print(f"\n******You lose, correct number was: {random_number}******")


import random
play_agin = "y"
while play_agin == "y":
    game()
    play_agin = input('Do yoy wont to play agin "y" or "n"?: ').lower()
    if play_agin == "y":
        print("\n" *40)

print("thank you for playing")
