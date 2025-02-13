import art
import random
from game_data import data

def randomizing(list_of_random_numbers):
    while True:
        rand = random.randint(0, len(data)-1)
        if rand not in list_of_random_numbers:
            return rand

def guessing(list_of_random):
    while True:
        print(f"Compare A: {data[list_of_random[-2]]["name"]}, {data[list_of_random[-2]]["description"]}, from {data[list_of_random[-2]]["country"]}\n {art.vs}")
        print(f"or B: {data[list_of_random[-1]]["name"]}, {data[list_of_random[-1]]["description"]}, from {data[list_of_random[-1]]["country"]} ")
        guess_check = input('Who is mor popular "A" or "B"?: ')
        if guess_check == "a" or guess_check == "b":
            return guess_check
        else:
            print("Wrong intput, try agin")
            print("\n" * 40)


def compare(list_of_random,information):
    if information == "a":
        if data[list_of_random[-2]]["follower_count"] > data[list_of_random[-1]]["follower_count"]:
            return True
        elif data[list_of_random[-2]]["follower_count"] == data[list_of_random[-1]]["follower_count"]:
            return True
        else:
            return False
    else:
        if data[list_of_random[-2]]["follower_count"] < data[list_of_random[-1]]["follower_count"]:
            return True
        elif data[list_of_random[-2]]["follower_count"] == data[list_of_random[-1]]["follower_count"]:
            return True
        else:
            return False



play_agin = "y"
while play_agin == "y":
    print(art.logo)
    list_of_randoms = []
    list_of_randoms.append(randomizing(list_of_randoms))
    list_of_randoms.append(randomizing(list_of_randoms))
    points=0
    continuity = True
    while continuity:
        guess=guessing(list_of_randoms)
        continuity=compare(list_of_randoms,guess)
        if continuity:
            points +=1
            print("\n" * 40)
            print("You have guessed correctly!")
            print(f"Your currents score is {points}")
            list_of_randoms.append(randomizing(list_of_randoms))
        if points == 49:
            continuity = False
    if points == 49:
        print(f"****Impossible you have guessed everything good job, you have all {points} pairs!!!****")
    else:
        print(f"****Game over, you have made a wrong gues, you have gained {points} points****")
    play_agin=input('would you like to play agin "y" or "n"?: ')
    print("\n" * 40)
print("Thank you for playing")