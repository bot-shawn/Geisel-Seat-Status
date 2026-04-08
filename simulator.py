import sqlite3
import random
import time
from datetime import datetime

DB_PATH = 'data/geisel_seats.db'
# We want to be able to simulate the data moving around

def start_simulation():
    print('Simulation Starting press control + c to stop simulation')

    while True:
        try:
            with sqlite3.connect(DB_PATH) as conn:
                cursor = conn.cursor()

                floor_id = random.choice([1, 2, 4, 8])

                change = random.randint(-5, 5)

                cursor.execute('''
                               UPDATE floor_status
                               SET occupied_seats = MAX(0, MIN(total_seats, occupied_seats + ?)),
                                    last_updated = ?
                               WHERE floor_id = ?
                               ''', (change, datetime.now(), floor_id))
                conn.commit()
                print(f"Floor {floor_id}: Change of {change:+} seats.")

            time.sleep(3)

        except KeyboardInterrupt:
            print('simulation stopped by user')
            break

if __name__ == "__main__":
    start_simulation()