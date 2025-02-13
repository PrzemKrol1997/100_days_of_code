import random
name_list=input("Enter names of all the people separated by spaces \n").split()
list_length =len(name_list)
print(f"{name_list[random.randint(0, list_length - 1)]} pays the bill")