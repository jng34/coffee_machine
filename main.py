from os import system, name
from art import logo
from info import MENU, resources

################################
def clear():
    """Function to clear console"""
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux
    else:
        _ = system('clear')
################################



# MENU = {
#     "espresso": {
#         "ingredients": {
#             "water": 50,
#             "coffee": 18,
#         },
#         "cost": 1.5,
#     },
#     "latte": {
#         "ingredients": {
#             "water": 200,
#             "milk": 150,
#             "coffee": 24,
#         },
#         "cost": 2.5,
#     },
#     "cappuccino": {
#         "ingredients": {
#             "water": 250,
#             "milk": 100,
#             "coffee": 24,
#         },
#         "cost": 3.0,
#     }
# }

# resources = {
#     "water": 1000,
#     "milk": 800,
#     "coffee": 500,
# }

w, m, c = resources
money_earned = 0


# All Functions
# TODO: Check if resources are sufficient?
def check_resources(user_choice):
  """Checks to see if there's enough resources and prints a statement if no."""
  menu = MENU[user_choice]['ingredients']
  items = ['water', 'coffee', 'milk']
  for item in items:
      if item in menu and menu[item] > resources[item]:
          print(f"Sorry there is not enough {item}.")
          start_coffee_machine()


# TODO: Print report.
def print_report():
  print(f"""
  Water: {resources[w]} mL\n
  Milk: {resources[m]} mL\n
  Coffee: {resources[c]} mL\n
  Money: ${money_earned: 0.2f}\n
  """)
  start_coffee_machine()


# TODO: Process coins.
def process_coins():
  print("Please insert coins.")
  quarters = int(input('How many quarters?: '))
  dimes = int(input('How many dimes?: '))
  nickels = int(input('How many nickels?: '))
  pennies = int(input('How many pennies?: '))

  total = .25 * quarters + .10 * dimes + .05 * nickels + .01 * pennies
  return round(total, 2)


# TODO: Check if transaction is successful?
def transaction_check(user_amount, user_choice):
  global money_earned
  item_cost = MENU[user_choice]['cost']
  if user_amount >= item_cost:
      money_earned += item_cost
      change = user_amount - item_cost
      make_coffee(user_choice)
      return f"Here is ${round(change, 2)} in change.\n" \
              f"Here is your latte ☕. Enjoy!"
  else:
      return "Sorry that's not enough. Money refunded."


# TODO: Make coffee.
def make_coffee(user_choice):
  ingredients = MENU[user_choice]['ingredients']
  for item in ingredients:
      amount_used = ingredients[item]
      resources[item] -= amount_used


# TODO: Run coffee machine.
def start_coffee_machine():
  """Main code base that calls all other functions to run coffee machine"""
  choice = input("What would you like? (espresso/latte/cappuccino): ")
  if choice == 'report':
    print_report()
  # Turns off (exits) machine
  elif choice == 'off':
    quit()
  check_resources(choice)
  amount = process_coins()
  check = transaction_check(amount, choice)
  print(check)
  start_coffee_machine()


print(logo)
start_coffee_machine()
