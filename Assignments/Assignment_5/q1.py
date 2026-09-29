def greet_user(name): #function that takes a name parameter
    print(f"Hello, {name}! Welcome aboard.") #prints a statement greeting the user with their name
user_name = input("Enter your name: ") #tells the user to enter their name
greet_user(user_name) #calls greet_user function with the user_name