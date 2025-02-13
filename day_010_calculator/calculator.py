# Function will take number and then ask for operator and second number
# After calculating program will ask as if we want to continue with another number and operator or start over
from art import logo

def enter_a_number():
    while True:
        try:

            return float(input("enter a number: "))
        except ValueError:
            print("You have entered a wrong number, pleas try agin: ")


def enter_operator():
    while True:
        new_operator = input("enter an operator: \n+\n-\n*\n/\n  ")
        if new_operator == "+" or new_operator == "-" or new_operator =="*" or new_operator =="/":
            return new_operator
        print("wrong operator try agin")


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return round(n1 / n2,2)


print(logo)
operation_sum = 0
continuity = "n"
functions = {
    "+":add,
    "-":subtract,
    "/":divide,
    "*":multiply,
}
while continuity == "y" or continuity =="n":
    if continuity =="n":
        operation_sum = 0
    if continuity =="n":
        number1 = enter_a_number()
    else:
        number1 = operation_sum
    operator = enter_operator()
    number2 = enter_a_number()
    operation_sum=functions[operator](number1,number2)
    print(f"{number1} {operator} {number2} = {operation_sum}")
    continuity = input('Continue calculating with previous answer? "y"\nStart over? "n"\nExit "x"\n  ').lower()
    if continuity == "n":
        print("\n" * 40)
        print(logo)
print("Thank you for participating, have a nice day!")