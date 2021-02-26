MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}


def update_resources(drink):
    for key in resources:
        if key != "money":
            resources[key] -= drink["ingredients"][key]
        else:
            resources[key] += drink["cost"]


def process_coins():
    amount = 0
    print("Please insert coins.")
    amount += int(input("How many quarters?: ")) * 0.25
    amount += int(input("How many dimes?: ")) * 0.10
    amount += int(input("How many nickles?: ")) * 0.05
    amount += int(input("How many pennies?: ")) * 0.01
    return amount


def print_report():
    for key in resources:
        string = f"{key}: "
        if key == "money":
            string += f"${resources[key]}"
        elif key == "coffee":
            string += f"{resources[key]}g"
        else:
            string += f"{resources[key]}ml"

        print(string)


def process_request():
    # limitations is a list of resources we don't have enough of
    limitations = []
    drink = MENU[request]

    # find limitations
    for key in resources:
        if key != "money" and resources[key] < drink["ingredients"][key]:
            limitations.append(key)

    # if there are limitations, print them
    if len(limitations) != 0:
        string = "Sorry but there is not enough "
        if len(limitations) == 1:
            string += f"{limitations[0]}"

        for i in limitations:
            if limitations[-1] == i:
                string += f"and {i}"
            elif limitations[-2] == i:
                string += f"{i} "
            else:
                string += f"{i}, "
        print(string)
        return

    # find total money entered
    amount = process_coins()
    # if there is enough money
    if amount >= drink["cost"]:
        # calculate change
        change = amount - drink["cost"]
        # if there is change, return in
        if change != 0:
            print(f"Here is ${round(change, 2)} dollars in change.")
        update_resources(drink)
        print(f"Here is your {request}. Enjoy!")
    else:
        print("Sorry but that's not enough money. Money refunded.")
        return


while True:
    request = input("What would you like? (espresso/latte/cappuccino): ")
    # Turn off
    if request == "off":
        break
    # Print report
    elif request == "report":
        print_report()

    # Process request
    if request in MENU:
        process_request()
