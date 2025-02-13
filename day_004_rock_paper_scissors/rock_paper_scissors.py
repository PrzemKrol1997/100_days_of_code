# player chooses rock, paper or scissors and program chooses at random then compare as per rules
# asks player if he would like to play agin
import random

def display_choice(choice):
    if choice == 0:
        print(("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""))
    elif choice == 1:
        print(("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""))
    elif choice == 2:
        print(("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""))


a=1
while a == 1:
    try:
        choice1 = int(input("Enter 0-rock, 1-paper, 2-scissors: "))
    except ValueError:
        choice1 = 5
    if 0<= choice1 <= 2:
        print("Your choice: ")
        display_choice(choice1)
        game_choice=random.randint(0,2)
        print(f"Game choice: ")
        display_choice(game_choice)
        if choice1 == game_choice:
            print("draw")
        elif choice1 == 0 and game_choice == 1 :
            print ("Paper beats rock, you lose")
        elif choice1 == 0 and game_choice == 2:
            print("Rock beats scissors, you win")
        elif choice1 == 1 and game_choice == 2:
            print("scissors beats paper, you lose")
        elif choice1 == 1 and game_choice == 0:
            print("Paper beats rock, you win")
        elif choice1 == 2 and game_choice == 0:
            print("Rock beats scissors, you lose")
        elif choice1 == 2 and game_choice == 1:
            print("scissors beats paper, you win")
    else:
        print("Wrong insert, game over")
    try:
        a=int(input("type 1 if you want to play agin play agin: "))
    except ValueError:
        a=2
print("Thank you for playing")