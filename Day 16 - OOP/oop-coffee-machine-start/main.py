from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machine = CoffeeMaker()
menu = Menu()
money = MoneyMachine()

items = menu.get_items()

on = True
while on:
    selection = input(f"What would you like? ({items}):")

    if selection == "off":
        on = False
        quit()
    elif selection == "report":
        machine.report()
        money.report()
    else:
        drink = menu.find_drink(selection)
        if machine.is_resource_sufficient(drink):
            if money.make_payment(drink.cost):
                machine.make_coffee(drink)
            else:
                quit()