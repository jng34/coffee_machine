from art import logo
from info import MENU, resources


w, m, c = resources
profit = 0

# All Functions
def check_resources(user_choice):
  """Checks to see if there's enough resources and prints a statement if no."""
  menu = MENU[user_choice]['ingredients']
  items = ['water', 'coffee', 'milk']
  for item in items:
      if item in menu and menu[item] > resources[item]:
          print(f"Sorry there is not enough {item}.")
          start_coffee_machine()


def print_report():
  print(f"""
  Water: {resources[w]} mL\n
  Milk: {resources[m]} mL\n
  Coffee: {resources[c]} mL\n
  Money: ${profit: 0.2f}\n
  """)
  start_coffee_machine()


def process_coins():
  print("Please insert coins.")
  quarters = int(input('How many quarters?: '))
  dimes = int(input('How many dimes?: '))
  nickels = int(input('How many nickels?: '))
  pennies = int(input('How many pennies?: '))

  total = .25 * quarters + .10 * dimes + .05 * nickels + .01 * pennies
  return round(total, 2)


def transaction_check(user_amount, user_choice):
  global profit
  item_cost = MENU[user_choice]['cost']
  if user_amount >= item_cost:
    profit += item_cost
    change = user_amount - item_cost
    print(f"Here is ${round(change, 2)} in change.")
    return True
  else:
    print("Sorry that's not enough. Money refunded.")
    return False


def make_coffee(user_choice):
  ingredients = MENU[user_choice]['ingredients']
  for item in ingredients:
    resources[item] -= ingredients[item]
  print(f"Here is your {user_choice} ☕. Enjoy!")


def start_coffee_machine():
  """Main code base that calls all other functions to run coffee machine"""
  choice = input("What would you like? (espresso/latte/cappuccino): ")
  if choice == 'off':
    quit()
  elif choice == 'report':
    print_report()
  else:
    check_resources(choice)
    amount = process_coins()
    if transaction_check(amount, choice):
      make_coffee(choice)
      start_coffee_machine()


print(logo)
start_coffee_machine()
