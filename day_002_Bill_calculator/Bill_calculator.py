# The program asks how much you have to pay.
# It asks how much you would like to tip.
# It asks how many ways the bill will be split.
# The program calculates and tells how much each person has to pay.

print("Welcome to the tip calculator")
receipt=float(input("How much is the total bill?: $"))
tip=int(input("How much would you like to tip?: %"))
people=int(input("How many people are splitting the bill?"))
price = round(receipt * (1+tip/100) /people, 2)
print(f"Each person has to pay ${price}")


