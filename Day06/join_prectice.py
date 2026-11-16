import sqlite3

# Connect to a new database (this will be created in the day06 folder)
conn = sqlite3.connect("day06/company_join.db")
cursor = conn.cursor()

# 1. Create the departments table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS departments (
        dept_id INTEGER PRIMARY KEY,
        dept_name TEXT
    )
""")

# 2. Create the employees table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS employees (
        emp_id INTEGER PRIMARY KEY,
        name TEXT,
        dept_id INTEGER
    )
""")

# 3. Insert departments (1=Engineering, 2=Design)
cursor.execute("INSERT OR IGNORE INTO departments (dept_id, dept_name) VALUES (1, 'Engineering')")
cursor.execute("INSERT OR IGNORE INTO departments (dept_id, dept_name) VALUES (2, 'Design')")

# 4. Insert employees (Notice dept_id links to the departments table)
cursor.execute("INSERT OR IGNORE INTO employees (name, dept_id) VALUES ('Alice', 1)")
cursor.execute("INSERT OR IGNORE INTO employees (name, dept_id) VALUES ('Bob', 2)")
cursor.execute("INSERT OR IGNORE INTO employees (name, dept_id) VALUES ('Charlie', 1)")

conn.commit()
print("Tables created and data inserted!")

# 5. THE JOIN: Combine the two tables to see the department names!
print("\n--- EMPLOYEES AND THEIR DEPARTMENTS ---")
cursor.execute("""
    SELECT employees.name, departments.dept_name
    FROM employees
    JOIN departments ON employees.dept_id = departments.dept_id
""")

results = cursor.fetchall()
for row in results:
    print(f"{row[0]} works in {row[1]}")

print("\n--- DATA FROM THE CSV LOADED INTO THE DB ---")
# Connect to the new staff.db database
staff_conn = sqlite3.connect("day06/staff.db")
staff_cursor = staff_conn.cursor()

staff_cursor.execute("SELECT name, salary FROM staff WHERE role = 'Engineer'")
engineers = staff_cursor.fetchall()

for eng in engineers:
    print(eng)

print("\n--- AVERAGE ENGINEER SALARY ---")
staff_cursor.execute("SELECT AVG(salary) FROM staff WHERE role = 'Engineer'")
avg_salary = staff_cursor.fetchone()  # fetchone() gets just the first result

print(f"The average engineer salary is: {avg_salary[0]}")

staff_conn.close()

conn.close()