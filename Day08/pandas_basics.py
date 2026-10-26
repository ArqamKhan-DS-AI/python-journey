import pandas as pd

#1. Loads data from csv into a DataFrame
df = pd.read_csv("Day08/data.csv")

#2. Looks at the first 3 rows 
print("--- Head(first 3 rows) ---")
print(df.head(3))

#3. Get basic information about columns and data types
print("\n--- Info ---")
print(df.info())

#4. Get statistical summary (mean, min, max, etc.)
print("\n--- Describe(statistics) ---")
print(df.describe())

#5. Get the salaries only
print("\n--- JUST THE SALARIES ---")
print(df["salary"])

# 1. Create the filter (This creates a list of True/False for every row)
is_engineer = df["role"] == "Engineer"

# 2. Apply the filter to the DataFrame
engineers_df = df[is_engineer]

print("\n--- ONLY THE ENGINEERS ---")
print(engineers_df)

print("\n--- AVERAGE SALARY BY ROLE ---")
# Group the data by the 'role' column, then calculate the mean of the 'salary' column
avg_salary_by_role = df.groupby("role")["salary"].mean()

print(avg_salary_by_role)

high_earners = df[df["salary"] > 70000]
print(high_earners[["name", "salary"]])