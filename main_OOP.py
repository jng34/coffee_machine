from art import logo
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


coffee_machine = CoffeeMaker()
cash_register = MoneyMachine()
coffee_menu = Menu()


is_on = True
print(logo)
while is_on is not False:
    options = coffee_menu.get_items()
    choice = input(f"What would you like? ({options}): ")

    if choice == 'off':
        print('See you next time.')
        is_on = False
    elif choice == 'report':
        coffee_machine.report()
        cash_register.report()
    else:
        beverage = coffee_menu.find_drink(choice)
        if coffee_machine.is_resource_sufficient(beverage) and cash_register.make_payment(beverage.cost):
            coffee_machine.make_coffee(beverage)


