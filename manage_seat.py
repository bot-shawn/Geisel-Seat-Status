import sqlite3
from datetime import datetime

# The path to our database
DB_PATH = 'data/geisel_seats.db'

# Reading function
def get_lib_status():
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        # We want to grab the specific columns. We only want the data we actually need.
        cursor.execute('''
                       SELECT floor_id, floor_name, occupied_seats, total_seats, noise_level
                       FROM floor_status
                       ''')
        # We use this to turn all the rows found by sql and make them into a python list, so our app can display it
        return cursor.fetchall()
    
# Writing function (we want to use this to update the table)
# the variable change is the key, if a student sit down we pass 1 and if they leave we pass -1
def update_seats(floor_id, change):
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        # This tells SQL that we want to change the exisiting data by using UPDATE.
        # The max and min logic is to ensure that we never have a number of seats on each floor that is impossible to 
        # happen. Where floor_id is to make sure we are changing the data for the right floor
        cursor.execute('''
                       UPDATE floor_status
                       SET occupied_seats = MAX(0, MIN(total_seats, occupied_seats + ?)),
                            last_updated = ?
                       WHERE floor_id = ?
                       ''', (change, datetime.now(), floor_id))
        
        # Testing function making sure everything is ok
if __name__ == "__main__":
    # Current status
    print("Current Status before update:")
    print(get_lib_status())

    # Simulating 20 students leaving the 2nd Floor
    print("\nAttempting to update Floor 2")
    update_seats(2, -20) 

    # The new status
    print("\nNew Status after update:")
    print(get_lib_status())