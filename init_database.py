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
            floor_id INTEGER,
            floor_name TEXT,
            floor_section TEXT,
            total_seats INTEGER,
            occupied_seats INTEGER,
            noise_level TEXT,
            has_outlets BOOLEAN,
            x_coord INTEGER,  
            y_coord INTEGER,
            last_updated DATETIME,
            PRIMARY KEY (floor_id, floor_section)
        )
    ''')

    # Clear the data without deleting the file
    print("Clearing old data")
    cursor.execute("DELETE FROM floor_status")

    # Entering the seed data for testing
    print("Setting up data")
    floors = [
        # 1st Floor 
        (1, '1st Floor (Quiet)', 'Lower Floor East', 150, 45, 'Quiet', 1, 75, 40, datetime.now()),
        (1, '1st Floor (Social)', 'Lower Floor West', 520, 110, 'Social', 1, 25, 60, datetime.now()),
        
        # 2nd Floor 
        (2, '2nd Floor (Main)', 'Geisel East', 620, 245, 'Social', 1, 80, 50, datetime.now()),
        (2, '2nd Floor (Main)', 'Geisel West', 460, 180, 'Social', 1, 20, 50, datetime.now()),
        
        # 4th Floor
        (4, '4th Floor (Quiet)', 'Call Numbers A-D', 20, 4, 'Quiet', 1, 30, 70, datetime.now()),
        (4, '4th Floor (Quiet)', 'Call Numbers D-HG', 20, 7, 'Quiet', 1, 70, 70, datetime.now()),
        (4, '4th Floor (Quiet)', 'Call Numbers HG-PL', 20, 3, 'Quiet', 1, 30, 30, datetime.now()),
        (4, '4th Floor (Quiet)', 'Call Numbers PL-ZA', 20, 11, 'Quiet', 1, 70, 30, datetime.now()),
        
        # 5th Floor 
        (5, '5th Floor (Quiet)', 'Call Numbers A-BS', 40, 12, 'Quiet', 1, 30, 70, datetime.now()),
        (5, '5th Floor (Quiet)', 'Call Numbers BT-DF', 40, 15, 'Quiet', 1, 70, 70, datetime.now()),
        (5, '5th Floor (Quiet)', 'Call Numbers DG-E', 35, 10, 'Quiet', 1, 30, 30, datetime.now()),
        (5, '5th Floor (Quiet)', 'Call Numbers E-F', 40, 18, 'Quiet', 1, 70, 30, datetime.now()),
        
        # 6th Floor 
        (6, '6th Floor (Quiet)', 'Call Numbers G-HD', 110, 45, 'Quiet', 1, 30, 70, datetime.now()),
        (6, '6th Floor (Quiet)', 'Call Numbers HD-JC', 110, 52, 'Quiet', 1, 70, 70, datetime.now()),
        (6, '6th Floor (Quiet)', 'Call Numbers JF-LG', 110, 40, 'Quiet', 1, 30, 30, datetime.now()),
        (6, '6th Floor (Quiet)', 'Oversized Materials', 110, 38, 'Quiet', 1, 70, 30, datetime.now()),
        
        # 7th Floor 
        (7, '7th Floor (Quiet)', 'Call Numbers P-PN', 50, 25, 'Quiet', 1, 30, 70, datetime.now()),
        (7, '7th Floor (Quiet)', 'Call Numbers PN-PQ', 50, 22, 'Quiet', 1, 70, 70, datetime.now()),
        (7, '7th Floor (Quiet)', 'Call Numbers PQ-PS', 45, 18, 'Quiet', 1, 30, 30, datetime.now()),
        (7, '7th Floor (Quiet)', 'Call Numbers PS-PT', 50, 28, 'Quiet', 1, 70, 30, datetime.now()),
        
        # 8th Floor 
        (8, '8th Floor (Silent)', 'Call Numbers Z4-Z253', 40, 38, 'Silent', 0, 30, 70, datetime.now()),
        (8, '8th Floor (Silent)', 'Call Numbers Z473-Z731', 40, 35, 'Silent', 0, 70, 70, datetime.now()),
        (8, '8th Floor (Silent)', 'Call Numbers Z731-Z2010', 45, 42, 'Silent', 0, 30, 30, datetime.now()),
        (8, '8th Floor (Silent)', 'Call Numbers Z2012-ZA', 40, 39, 'Silent', 0, 70, 30, datetime.now()),
    ]

    # Inserting in each rows
    print("INSERTING")
    cursor.executemany('INSERT INTO floor_status VALUES (?,?,?,?,?,?,?,?,?,?)', floors)

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