import csv
import sqlite3

def load_data(csv_file: str, db_file: str) -> None:
    """Reads the CSV and loads it into a SQLite database."""
    print(f"Loading data from {csv_file}...")
    
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    # Create the table (dropping it first so we start fresh every time we run)
    cursor.execute("DROP TABLE IF EXISTS employees")
    cursor.execute("""
        CREATE TABLE employees (
            id INTEGER PRIMARY KEY,
            name TEXT,
            role TEXT,
            salary INTEGER
        )
    """)

    # Read and insert the data
    with open(csv_file, mode="r", encoding="utf-8") as infile:
        reader = csv.DictReader(infile)
        for row in reader:
            cursor.execute(
                "INSERT INTO employees (id, name, role, salary) VALUES (?, ?, ?, ?)",
                (row["id"], row["name"], row["role"], row["salary"])
            )

    conn.commit()
    conn.close()
    print("Data loaded successfully into the database!\n")

def generate_report(db_file: str) -> None:
    """Queries the database and prints a summary report."""
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    print("=" * 40)
    print("       COMPANY DATA REPORT")
    print("=" * 40)

    # 1. Total number of employees
    cursor.execute("SELECT COUNT(*) FROM employees")
    total = cursor.fetchone()[0]
    print(f"Total Employees: {total}")

    # 2. Average salary
    cursor.execute("SELECT AVG(salary) FROM employees")
    avg_salary = cursor.fetchone()[0]
    print(f"Average Salary:  ${avg_salary:,.2f}")

    # 3. Highest paid employee
    cursor.execute("SELECT name, salary FROM employees ORDER BY salary DESC LIMIT 1")
    top_earner = cursor.fetchone()
    print(f"Highest Paid:    {top_earner[0]} (${top_earner[1]:,})")

    print("-" * 40)
    print("SALARY BY ROLE:")
    
    # 4. Group by role to see average salary per role
    cursor.execute("SELECT role, AVG(salary) FROM employees GROUP BY role")
    roles = cursor.fetchall()
    for role, avg in roles:
        print(f" - {role}: ${avg:,.2f}")

    print("=" * 40)
    conn.close()

if __name__ == "__main__":
    csv_path = "day07/data.csv"
    db_path = "day07/company_report.db"
    
    # Step 1: Load the data
    load_data(csv_path, db_path)
    
    # Step 2: Generate the report
    generate_report(db_path)