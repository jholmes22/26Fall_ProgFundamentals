# sensor_app_template.py - runs ON THE PC (regular Python 3, e.g. VS Code or IDLE)
# Template: talks to the board over USB serial and prints the readings.
# Rename a copy of this file (e.g. sensor_app.py) and extend it for the assignment.
#
# Setup: pip install pyserial
# IMPORTANT: close Thonny before running this, only one program can use the port.

import sqlite3
import time
import serial

PORT = "COM7"                      # <-- CHANGE to your board's port (see Device Manager)
BAUD = 115200


def ask_board(ser, command):
    """Send a one-letter command to the board and return the number it replies with."""
    ser.reset_input_buffer()                  # discard any stale data
    ser.write((command + "\n").encode())      # send command + newline
    # Read lines until one starts with DATA (ignores any boot messages)
    while True:
        line = ser.readline().decode(errors="ignore").strip()
        if line == "":
            raise TimeoutError("No reply from board")
        if line.startswith("DATA,"):
            return float(line.split(",")[2])

class DatabaseManager: #class to manage the database
    def __init__ (self, db_name):
        self.con = sqlite3.connect(db_name)
        self.con.execute("""DROP TABLE IF EXISTS sensor_data""") #Drop the table if it exists to start fresh each time
        self.con.execute("""
            CREATE TABLE IF NOT EXISTS sensor_data (
            id Integer PRIMARY KEY,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            sensor_type VARCHAR(30),
            sensor_reading_value FLOAT ) """)
    def log_history(self, sensor_type, sensor_reading_value): #function to log the data into the database
        with self.con:
            self.con.execute(""" INSERT INTO sensor_data(sensor_type, sensor_reading_value) VALUES (?, ?) """, (sensor_type, sensor_reading_value))
    def get_history(self): #function to get the data from the database
        with self.con:
            return self.con.execute("""SELECT * FROM sensor_data""").fetchall() #fetchall() returns a list of tuples, each tuple is a row in the table
        
def temperature(ser, db_manager): #function to get the temperature from the board and log it into the database
    temp = ask_board(ser, "T") #get the temperature from the board
    print(f"temperature: {temp:.1f} C")
    db_manager.log_history("Temperature", temp) #logs the temperature into the database
    

def humidity(ser, db_manager): #function to get the humidity from the board and log it into the database
    humidity = ask_board(ser, "H") #get the humidity from the board
    print(f"humidity: {humidity:.1f} %") #prints the humidity to the console
    db_manager.log_history("Humidity", humidity)

def main():
    # Open the serial port; opening it may reset the board, so wait a moment
    ser = serial.Serial(PORT, BAUD, timeout=5)
    time.sleep(2)
    ser.reset_input_buffer()
    db_manager = DatabaseManager("sensor_data.db") #define the database manager object to manage the database
    while True:
        print("Please choose from the following options:")
        print("T = temperature")
        print("H = humidity") #print the options to the console
        print("0 = Both")
        print("V = View Log History")
        choice = input("Enter your choice: ").lower() #get the user input and convert it to lowercase
        if choice == "t":
            temperature(ser, db_manager)
        elif choice == "h":
            humidity(ser, db_manager)
        elif choice == "0": #if the user chooses 0, get both temperature and humidity
            temperature(ser, db_manager)
            humidity(ser, db_manager)
        elif choice == "v": #if the user chooses v, get the history from the database and print it to the console
            history = db_manager.get_history()
            for row in history:
                print(row)
        else:
            print("Invalid choice. Please try again.") #if the user input is invalid, print an error message and ask for input again

if __name__ == "__main__":
    main()