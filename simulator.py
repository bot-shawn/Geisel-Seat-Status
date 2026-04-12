import sqlite3
import random
import time
from datetime import datetime

def start_simulation():
    conn = sqlite3.connect('data/geisel_seats.db')
    cursor = conn.cursor()
    print("Simulation Starting... Ctrl+C to stop")

    try:
        while True:
            # Get all available sections from the database
            cursor.execute("SELECT floor_id, floor_section, total_seats, occupied_seats FROM floor_status")
            sections = cursor.fetchall()
            
            # Pick a random section to update
            floor_id, section_name, total, current = random.choice(sections)
            
            # Simulating people coming (+1 to +3) or leaving (-1 to -3)
            change = random.randint(-3, 3)
            
            # Update the DB for that specific SECTION
            cursor.execute('''
                UPDATE floor_status 
                SET occupied_seats = MAX(0, MIN(total_seats, occupied_seats + ?)),
                    last_updated = ?
                WHERE floor_id = ? AND floor_section = ?
            ''', (change, datetime.now(), floor_id, section_name))
            
            conn.commit()
            
            # Print status so you can see it's working
            direction = "arrived at" if change > 0 else "left"
            print(f"{abs(change)} students {direction} {section_name} (Floor {floor_id})")
            
            # Wait a second before the next simulation
            time.sleep(1)

    except KeyboardInterrupt:
        print("Simulation stopped.")
        conn.close()

if __name__ == "__main__":
    start_simulation()