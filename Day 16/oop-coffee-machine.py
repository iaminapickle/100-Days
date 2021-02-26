from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

def process_coins():
    amount = 0
    print("Please insert coins.")
    amount += int(input("How many quarters?: ")) * 0.25
    amount += int(input("How many dimes?: ")) * 0.10
    amount += int(input("How many nickles?: ")) * 0.05
    amount += int(input("How many pennies?: ")) * 0.01
    return amount

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

while (True):
    drink = input("What would you like? (espresso/latte/cappuccino): ")

    if (drink == "report"):
        coffee_maker.report()
        money_machine.report()
    elif (drink == "off"):
        break
    elif (menu.find_drink(drink) != None):
        drink = menu.find_drink(drink)
        if (coffee_maker.is_resource_sufficient(drink)):
            if money_machine.make_payment(drink.cost) == False:
                print("Sorry that's not enough money. Money refunded.")
            else:
                coffee_maker.make_coffee(drink)
