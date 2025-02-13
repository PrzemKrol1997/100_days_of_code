import random
def password_expectancy(name):
    while True:
        try:
            name = int(input(f"How many {name} would you like in your password: "))
            return name
        except ValueError:
            print("Invalid input. Please enter a number.")

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Password generator")
number_of_letters = "letters"
number_of_symbols = "symbols"
number_of_numbers = "numbers"
number_of_letters = password_expectancy(number_of_letters)
number_of_symbols = password_expectancy(number_of_symbols)
number_of_numbers = password_expectancy(number_of_numbers)

password=[]
for i in range(number_of_letters):
    password.append(random.choice(letters))
for i in range(number_of_symbols):
    password.append(random.choice(symbols))
for i in range(number_of_numbers):
    password.append(random.choice(numbers))

print(f"Sorted password {''.join(password)}")
random.shuffle(password)
print(f"Unsorted password {''.join(password)}")