import sqlite3

# 1. Connect to the database (creates a file called company.db if it doesn't exist)
conn = sqlite3.connect("day05/company.db")

# A cursor is like a pen we use to write commands to the database
cursor = conn.cursor()

# 2. Create a table named 'employees'
# "IF NOT EXISTS" prevents an error if we run this script multiple times
cursor.execute("""
    CREATE TABLE IF NOT EXISTS employees (
        id INTEGER PRIMARY KEY,
        name TEXT,
        role TEXT,
        salary INTEGER
    )
""")
cursor.execute("INSERT INTO employees (name, role, salary) VALUES ('Alice', 'Engineer', 70000)")
cursor.execute("INSERT INTO employees (name, role, salary) VALUES ('Bob', 'Designer', 60000)")
cursor.execute("INSERT INTO employees (name, role, salary) VALUES ('Charlie', 'Engineer', 80000)")
cursor.execute("INSERT INTO employees (name, role, salary) VALUES ('Diana', 'Manager', 90000)")
conn.commit() # Save the changes
print("Database connected and table created!")