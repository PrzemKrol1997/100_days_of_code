# program checks if someone can buy a ticket and calculates how much will it cost him

height=int(input("Enter your height"))
price = 0
if height < 120:
    print("You must grow up before you can enter: ")
else:
    age = int(input("Enter your age: "))
    if age <= 12:
        price += 5
    elif 18 > age:
        price += 7
    elif   45 <= age <= 55:
        print("everything is gonna be alright, have a ticket on the house")
    else:
        price +=12

    photo = input("do You wont to buy a ticket, yes or no: ")
    if photo == "yes":
        price += 3
    print (f"Total cost: ${price}")