import sqlite3
import csv
import os


DB_NAME = "water_points.db"
CSV_FILE = "data/sample_data.csv"


def create_database():

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS readings (

            reading_id INTEGER PRIMARY KEY AUTOINCREMENT,

            waterpoint_id TEXT NOT NULL,

            habitation TEXT NOT NULL,

            flow_ok TEXT NOT NULL,

            usage_count INTEGER NOT NULL,

            recorded_at TEXT NOT NULL

        )
    """)

    conn.commit()

    print("Database table created successfully!")

    # Check whether data already exists
    cursor.execute("SELECT COUNT(*) FROM readings")

    count = cursor.fetchone()[0]

    # Import CSV only if database is empty
    if count == 0:

        if os.path.exists(CSV_FILE):

            with open(
                CSV_FILE,
                "r",
                encoding="utf-8"
            ) as file:

                reader = csv.DictReader(file)

                for row in reader:

                    cursor.execute("""
                        INSERT INTO readings
                        (
                            waterpoint_id,
                            habitation,
                            flow_ok,
                            usage_count,
                            recorded_at
                        )
                        VALUES (?, ?, ?, ?, ?)
                    """, (

                        row["waterpoint_id"],
                        row["habitation"],
                        row["flow_ok"],
                        int(row["usage_count"]),
                        row["recorded_at"]

                    ))

            conn.commit()

            print("Sample readings imported successfully!")

        else:

            print(
                "sample_data.csv not found!"
            )

    else:

        print(
            f"Database already contains {count} readings."
        )

    conn.close()


if __name__ == "__main__":

    create_database()