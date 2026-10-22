import sqlite3

# 1. Connect to the existing database
conn = sqlite3.connect("day05/company.db")
cursor = conn.cursor()

print("--- ALL EMPLOYEES ---")
# SELECT * means "give me all columns"
cursor.execute("SELECT * FROM employees")
all_employees = cursor.fetchall()

for emp in all_employees:
    print(emp)

print("\n--- ONLY ENGINEERS ---")
# WHERE filters the rows
cursor.execute("SELECT name, salary FROM employees WHERE role = 'Engineer'")
engineers = cursor.fetchall()

for eng in engineers:
    print(f"Name: {eng[0]} | Salary: {eng[1]}")
print("\n--- HIGH EARNERS (Salary > 75,000) ---")
cursor.execute("SELECT name, salary FROM employees WHERE salary > 75000")
high_earners = cursor.fetchall()

for person in high_earners:
    print(person)
conn.close()