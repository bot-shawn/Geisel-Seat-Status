import sqlite3
import os
from datetime import datetime

def initialize():
    db_path = 'data/geisel_seats.db'
    
    # Check if directory exists
    if not os.path.exists('data'):
        os.makedirs('data')
        print("📁 Created 'data' directory")

    # Connect to the path for the database
    print(f"Connecting to {db_path}...")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Creating the Table format
    print("Creating table")
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS floor_status (
            floor_id INTEGER PRIMARY KEY,
            floor_name TEXT,
            total_seats INTEGER,
            occupied_seats INTEGER,
            noise_level TEXT,
            has_outlets BOOLEAN,
            last_updated DATETIME
        )
    ''')

    # Entering the seed data for testing
    print("Setting up data")
    floors = [
        (1, '1st Floor (Social)', 200, 120, 'Social', 1, datetime.now()),
        (2, '2nd Floor (Main)', 300, 290, 'Social', 1, datetime.now()),
        (4, '4th Floor (Quiet)', 150, 45, 'Quiet', 1, datetime.now()),
        (8, '8th Floor (Silent)', 100, 98, 'Silent', 0, datetime.now())
    ]
    # Inserting in each rows
    print("INSERTING")
    cursor.executemany('INSERT OR REPLACE INTO floor_status VALUES (?,?,?,?,?,?,?)', floors)    

    # commiting the tables
    conn.commit()
    print("COMMIT successful")

    # Tells me how many rows are there
    cursor.execute("SELECT COUNT(*) FROM floor_status")
    count = cursor.fetchone()[0]
    print(f"📊 Verification: There are {count} rows in the database.")

    # A force save button
    conn.close()
    print("🔌 Connection closed.")

# the initilization function
if __name__ == "__main__":
    initialize()