import time
from hs3003 import HS3003

sensor = HS3003() #allows board to read and display temp and humidity

print("Please choose from the following options:") #prints as a menu to choose from
print("T - Temperature")
print("H - Humidity")
print("0 - Both") #prints as an option for user
def temperature(): #function that uses temperature parameter
    t, h = sensor.read()
    print("Temp:", t) #prints the statement temp along with the temperature from the sensor
    
def humidity():
    t, h = sensor.read() #reads the humidity from the sensor
    print("Hum:", h)
    
while True:
    choice = input("enter your choice: ") #user chooses between the print statements at the top
    
    if choice == "T":
        temperature() #calls temperature function if T is enetered
        
    elif choice == "H":
        humidity() #calls humidity function is H is entered
        
    elif choice == "0": #states that if 0 is entered the output in both temp and hum
        temperature()
        humidity()
    
