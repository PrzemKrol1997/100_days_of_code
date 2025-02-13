from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def coffee_machine():
    my_coffee_machine = CoffeeMaker()
    my_money_machine = MoneyMachine()
    my_menu = Menu()
    while True:
        drink=input(f"what would you like to order {my_menu.get_items()} ").lower()
        if drink == "report":
            my_coffee_machine.report()
            my_money_machine.report()
        elif drink == "off":
            print("Turning off...")
            return
        else:
            drink = my_menu.find_drink(drink)
            if drink:
                if my_coffee_machine.is_resource_sufficient(drink):
                    if my_money_machine.make_payment(drink.cost):
                        my_coffee_machine.make_coffee(drink)




coffee_machine()