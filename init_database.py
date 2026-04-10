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
            last_updated DATETIME,
            PRIMARY KEY (floor_id, floor_section)
        )
    ''')

    # Entering the seed data for testing
    print("Setting up data")
    floors = [
        (1, '1st Floor (Social)', 'Lower Floor West', 200, 120, 'Social', 1, datetime.now()),
        (1, '1st Floor (Quiet)', 'Lower Floor East', 200, 120, 'Social', 1, datetime.now()),
        (2, '2nd Floor (Main)', 'Geisel East', 300, 290, 'Social', 1, datetime.now()),
        (2, '2nd Floor (Main)', 'Geisel West', 300, 290, 'Social', 1, datetime.now()),
        (4, '4th Floor (Quiet)', 'Call Numbers A-D', 150, 45, 'Quiet', 1, datetime.now()),
        (4, '4th Floor (Quiet)', 'Call Numbers D-HG', 150, 45, 'Quiet', 1, datetime.now()),
        (4, '4th Floor (Quiet)', 'Call Numbers HG-PL', 150, 45, 'Quiet', 1, datetime.now()),
        (4, '4th Floor (Quiet)', 'Call Numbers PL-ZA', 150, 45, 'Quiet', 1, datetime.now()),
        (5, '5th Floor (Quiet)', 'Call Numbers A-BS', 150, 50, 'Quiet', 1, datetime.now()),
        (5, '5th Floor (Quiet)', 'Call Numbers BT-DF', 150, 50, 'Quiet', 1, datetime.now()),
        (5, '5th Floor (Quiet)', 'Call Numbers DG-E', 150, 50, 'Quiet', 1, datetime.now()),
        (5, '5th Floor (Quiet)', 'Call Numbers E-F', 150, 50, 'Quiet', 1, datetime.now()),
        (6, '6th Floor (Quiet)', 'Call Numbers G-HD', 150, 60, 'Quiet', 1, datetime.now()),
        (6, '6th Floor (Quiet)', 'Call Numbers HD-JC', 150, 60, 'Quiet', 1, datetime.now()),
        (6, '6th Floor (Quiet)', 'Call Numbers JF-LG', 150, 60, 'Quiet', 1, datetime.now()),
        (6, '6th Floor (Quiet)', 'Oversized Materials', 150, 60, 'Quiet', 1, datetime.now()),
        (7, '7th Floor (Quiet)', 'Call Numbers P-PN', 150, 70, 'Quiet', 1, datetime.now()),
        (7, '7th Floor (Quiet)', 'Call Numbers PN-PQ', 150, 70, 'Quiet', 1, datetime.now()),
        (7, '7th Floor (Quiet)', 'Call Numbers PQ-PS', 150, 70, 'Quiet', 1, datetime.now()),
        (7, '7th Floor (Quiet)', 'Call Numbers PS-PT', 150, 70, 'Quiet', 1, datetime.now()),
        (8, '8th Floor (Silent)','Call Numbers Z4-Z253', 100, 98, 'Silent', 0, datetime.now()),
        (8, '8th Floor (Silent)','Call Numbers Z473-Z731', 100, 98, 'Silent', 0, datetime.now()),
        (8, '8th Floor (Silent)','Call Numbers Z731-Z2010', 100, 98, 'Silent', 0, datetime.now()),
        (8, '8th Floor (Silent)','Call Numbers Z2012-ZA', 100, 98, 'Silent', 0, datetime.now()),
    ]
    # Inserting in each rows
    print("INSERTING")
    cursor.executemany('INSERT OR REPLACE INTO floor_status VALUES (?,?,?,?,?,?,?,?)', floors)

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