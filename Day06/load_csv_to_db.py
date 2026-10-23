import csv
import sqlite3

def load_csv_to_sqlite(csv_file: str, db_file: str) -> None:
    # 1. Connect to the database
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    # 2. Create the table (if it doesn't exist)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS staff (
            id INTEGER PRIMARY KEY,
            name TEXT,
            role TEXT,
            salary INTEGER
        )
    """)

    # 3. Read the CSV
    with open(csv_file, mode="r", encoding="utf-8") as infile:
        reader = csv.DictReader(infile)
        
        # 4. Loop through each row and insert it
        count = 0
        for row in reader:
            cursor.execute(
                "INSERT INTO staff (id, name, role, salary) VALUES (?, ?, ?, ?)",
                (row["id"], row["name"], row["role"], row["salary"])
            )
            count += 1

    # 5. Save and close
    conn.commit()
    conn.close()
    print(f"Successfully loaded {count} rows from {csv_file} into {db_file}!")

if __name__ == "__main__":
    # Point to the Day 4 CSV file!
    csv_path = "day04/data.csv"
    db_path = "day06/staff.db"
    load_csv_to_sqlite(csv_path, db_path)