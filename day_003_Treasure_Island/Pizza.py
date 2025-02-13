# program calculates how much will the pizza cost based on user input

size= input("What size pizza do you want? S,M or L: ")
Pepperoni = input("Do you want Pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

if size == "L":
    price= 25
    if Pepperoni == "Y":
        price += 3
elif size == "M":
    price = 20
    if Pepperoni == "Y":
        price += 3
else:
    price = 15
    if Pepperoni == "Y":
        price += 2
if extra_cheese == "Y":
    price +=1
print(f"Your final bill is ${price}")