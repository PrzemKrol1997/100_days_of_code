from menue import MENU
from menue import resources

def which_drink ():
    while True:
        user_choice =  input('What would you like? (espresso "1"/latte "2"/cappuccino "3"): ')
        # special code for resources type 4 and 0 for off
        if user_choice == "1":
            return "espresso"
        elif user_choice == "2":
            return "latte"
        elif  user_choice == "3":
            return "cappuccino"
        elif user_choice ==  "4":
            return "resources"
        elif  user_choice ==  "0":
            return "off"
        else:
            print("Wrong input plies try agin")


def check_resources(drink_type,resources_count):
    lack_of =""
    if MENU[drink_type]["ingredients"]["water"] > resources_count["water"]:
        lack_of += "water "
    if MENU[drink_type]["ingredients"]["milk"] > resources_count["milk"]:
        lack_of += "milk "
    if MENU[drink_type]["ingredients"]["coffee"] > resources_count["coffee"]:
        lack_of += "coffe"
    return lack_of


def insert_coin(coin_type):
    count_of_coins = 0
    while True:
        try:
            count_of_coins = int(input(f"how many {coin_type}: "))
            return count_of_coins
        except ValueError:
            print("Wrong input plies try agin")


def pay_for_coffe(drink_type):
    print("insert coins.")
    quarters = "quarters"
    dimes = "dimes"
    nickles = "nickles"
    pennies = "pennies"
    print(f"You ned to pay {MENU[drink_type]["cost"]}")
    quarters = insert_coin(quarters)
    dimes = insert_coin(dimes)
    nickles = insert_coin(nickles)
    pennies = insert_coin(pennies)
    coin_sum = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
    rest = coin_sum - MENU[drink_type]["cost"]
    if rest > 0:
        print(f"Thank you for paying, pleas wait for coffee, hers rest: ${round(rest,2)}")
        print(f"Here is your {drink_type}. Enjoy!")
        return True
    else:
        return False

def change_resources(resources_current,drink_type):
    resources_current["water"] -= MENU[drink_type]["ingredients"]["water"]
    resources_current["milk"] -= MENU[drink_type]["ingredients"]["milk"]
    resources_current["coffee"] -= MENU[drink_type]["ingredients"]["coffee"]
    resources_current["money"] += MENU[drink_type]["cost"]
    return resources_current



def coffe_machine(resources_machine):
    drink = which_drink()
    if drink == "off":
        print("Turning off...")
        return
    elif drink == "resources":
        print (f"Water: {resources_machine["water"]}\nMilk: {resources_machine["milk"]}\nCoffe: {resources_machine["coffee"]}\nMoney: ${resources_machine["money"]}")
        coffe_machine(resources_machine)
    else:
        sufficient_resources = check_resources(drink,resources_machine)
        if sufficient_resources == "":
            if pay_for_coffe(drink):
                resources_machine = change_resources(resources_machine, drink)
                coffe_machine(resources_machine)
            else:
                print("Sorry that's not enough money. Money refunded.")
                coffe_machine(resources_machine)
        else:
            print(f"Sorry there is not enough {sufficient_resources}.")
            coffe_machine(resources_machine)

coffe_machine(resources)

