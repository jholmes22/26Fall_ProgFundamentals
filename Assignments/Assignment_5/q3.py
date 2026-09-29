def check_number(num): #function that takes a number parameter
    if int(num) % 2 == 0: #checks to see if the number is even or odd by dividing by 2 to see if there is a remainder
        print(f"{num} is an even number.")
    else:
        print(f"{num} is an odd number.") #prints if the number is odd because the remainder is not 0
number = input("Enter a number: ")
check_number(number) #calls the function with the number inputted by the user