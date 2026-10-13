from typing import Any


cafe_name = "*Python Cafe*"
print(cafe_name)
tax_rate = 0.08

menu = {  "espresso": 3.00,
    "latte": 4.50,
    "cappuccino": 4.25,
    "mocha": 5.00,
    "muffin": 2.50,
    "croissant": 3.25,
}

order = []

def greet(name):
    print(f"Welcome to Python cafe, {name}!")

customerName = input("What's your name?: ")
greet(customerName)
member = input("Are you a member? (yes/no):")
if member.lower()== "yes":
    is_member = True
else:
    is_member = False

def show_menu(menu):
    for item, price in menu.items():
        print(f"{item}: ${price:.2f}")

def show_order(order, menu):
   if len(order) == 0:
       print("Your order is empty.")
   else:
       for item in order:
          print(f"Your order is: {item} ${menu[item]:.2f}")
   print(f"You have {len(order)} item(s) in your order!")

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
    taxable_amount = subtotal - discount
    tax = taxable_amount * tax_rate
    total = subtotal - discount + tax
    print(f"== Python Cafe Receipt ==")
    print(f"Customer: {name}")
    for item in order:
        print(f"Your order is: {item} ${menu[item]:.2f}")
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Discount: -${discount:.2f}")
    print(f"Tax: ${tax:.2f}")
    print(f"Total: ${total:.2f}")
    if not is_member:
        print("Please join our rewards club to get exclusive discounts and offers!")
    print(f"Thank you for visiting Python Cafe {customerName}! We hope to see you again!")

while True:
    print("1. View Menu")
    print("2. Add Item to Order")
    print("3. Remove Item from Order")
    print("4. View Order")
    print("5. Checkout")

    choice = input("Select an option (1-5): ")

    if choice == "1":
        show_menu(menu)

    elif choice == "2":
        item = input("Enter the item you want to add: ").lower()
        if item in menu:
            quantity = int(input(f"How many? "))
            if quantity >= 1:
                for _ in range(quantity):
                    order.append(item)
                print(f"Your item was successfully added to your order!")
            else:
                print("Error: Quantity must be at least 1.")
        else:
            print("Error: Item is not on the menu.")

    elif choice == "3":
        item = input("Enter the item you want to remove: ").lower()
        if item in order:
            order.remove(item)
            print(f"Your item was successfully removed from your order.")
        else:
            print("That item is not in your order.")

    elif choice == "4":
        show_order(order, menu)

    elif choice == "5":
        if len(order) == 0:
            print("Your order is currently empty.")
            continue
        else:
            print_receipt(customerName, order, menu, is_member)
            break
    else:
        print("Invalid option. Please select a number from 1 to 5.")
        