with open("./input/letters/starting_letter.txt", mode="r") as letter:
    to_change_list = letter.read()


with open("./input/Names/names.txt", mode="r") as names:
    name_list = names.readlines()

for guest in name_list:
    guest = guest.strip()
    print (guest)
    with open(f"./Output/ReadyToSend/Letter_for_{guest}.txt", mode="w") as to_send:
        new_list = to_change_list.replace("[name]",f"{guest}")
        to_send.write(new_list)



