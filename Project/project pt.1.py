from typing import Any


cafe_name = "Python cafe"
tax_rate = 0.08

menu = {  "espresso": 3.00,
    "latte": 4.50,
    "cappuccino": 4.25,
    "mocha": 5.00,
    "muffin": 2.50,
    "croissant": 3.25,
}

order = ["latte", "muffin"]

def greet(name):
    print(f"Welcome to Python cafe, {name}!")

customerName = input("What's your name?: ")
greet(customerName)

def show_menu(menu):
    for item, price in menu.items():
        print(f"{item}: ${price:.2f}")
show_menu(menu)

def show_order(order, menu):
   if not order:
       print("Your order is empty.")
   else:
       for item in order:
          print(f"Your order is: {item} ${menu[item]:.2f}")
          length = len(order)
          print(f"You have {length} item(s) in your order!")
show_order(order,menu)

def calculate_subtotal(order, menu):
    subtotal = 0
    for item in order:
        subtotal += menu[item]
    return subtotal
print(f"Order Subtotal: ${calculate_subtotal(order, menu):.2f}")

def get_discount(subtotal, is_member):
   if is_member and subtotal >= 20:
       return subtotal * 0.15
   elif is_member and subtotal >= 10:
       return subtotal * 0.10
   elif not is_member and subtotal >= 25:
       return subtotal *0.05
   else:
       return 0.0

def print_receipt(name, order, menu, is_member):
    subtotal = calculate_subtotal(order, menu)
    discount = get_discount(subtotal, is_member)
    tax = subtotal * tax_rate
    total = subtotal - discount + tax