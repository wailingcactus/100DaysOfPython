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
    "money": 0
}



# TODO: Prompt user to ask what they would like
def coffee_machine():
    selection = input ("What would you like? (espresso/latte/cappuccino): ")

    # TODO: Print report of all coffee machine resources

    if selection == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${resources['money']}")
        coffee_machine()

    # TODO: Turn coffee machine off via "off"

    elif selection == "off":
        stop = True
        quit()
    else:

        price = MENU[selection]["cost"]
        water_used = MENU[selection]["ingredients"]["water"]
        if selection == "latte" or selection == "cappuccino":
            milk_used = MENU[selection]["ingredients"]["milk"]
        else:
            milk_used = 0
        coffee_used = MENU[selection]["ingredients"]["coffee"]



    # TODO: Check resources of coffee machine

        if water_used > resources["water"]:
            print("Sorry there is not enough water.")
            coffee_machine()
        elif milk_used > resources["milk"]:
            print("Sorry there is not enough milk.")
            coffee_machine()
        elif coffee_used > resources["coffee"]:
            print("Sorry there is not enough coffee.")
            coffee_machine()


    # TODO: Process coins

        # Prompt the user to insert coins
        print("Please insert coins.")

        quarters = int(input("How many quarters?: "))
        dimes = int(input("How many dimes?: "))
        nickels = int(input("How many nickels?: "))
        pennies = int(input("How many pennies?: "))

        total_paid = quarters * .25 + dimes * .10 + nickels * .05 + pennies * .01
        print(f"Total amount paid is ${total_paid}")



    # TODO: Check if transaction was successful
        if total_paid >= price:
            change = total_paid - price
            print (f"Here is ${change} in change.")
        else:
            print("Sorry that's not enough money. Money refunded")
            coffee_machine()

    # TODO: Make coffee and deduct resources
        resources["money"] += price
        resources["water"] -= water_used
        resources["milk"] -= milk_used
        resources["coffee"] -= coffee_used

stop = False

while not stop:
    coffee_machine()