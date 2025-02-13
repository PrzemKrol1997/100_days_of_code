
# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary


from art import logo


another_bet = "y"
better = {}
while another_bet == "y":
    print(logo)
    name =input("What is your name: ")
    bet = int(input("how much are you willing to bet: $"))
    better[name] = bet
    another_bet = input("is there another person willing to bet? Y or N?: ").lower()
    print("\n"*40)

highest_bet = 0
highest_bet_name ="noone"
# print(better, "\n")

for key in better:
    # print("highest_bet=", highest_bet, "\nkey=", key, "\nbetter[key]=", better[key], "\n")
    if better[key] > highest_bet:
        highest_bet_name = key
        highest_bet = better[key]
    elif better[key] == highest_bet:
        highest_bet_name +=" " + key

print(logo)
print("highest better is: ", highest_bet_name,". He/She is willing to bet: $", better[highest_bet_name])