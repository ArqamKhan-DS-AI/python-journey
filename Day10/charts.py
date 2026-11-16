import pandas as pd
import matplotlib.pyplot as plt

# 1. Load the data
df = pd.read_csv("day10/data.csv")

# 2. Group by role and calculate the average salary
avg_salary = df.groupby("role")["salary"].mean()

# 3. Create the bar chart
plt.figure(figsize=(8, 5))  # Width, Height in inches
plt.bar(avg_salary.index, avg_salary.values, color="skyblue")

# 4. Add labels and a title
plt.title("Average Salary by Role", fontsize=16)
plt.xlabel("Role", fontsize=12)
plt.ylabel("Average Salary ($)", fontsize=12)

# 5. Save the chart as an image and display it
plt.savefig("day10/bar_chart.png")
plt.show()

# 1. Create the line chart
plt.figure(figsize=(8, 5))
plt.plot(df["name"], df["salary"], marker="o", color="green", linestyle="--")

# 2. Add labels and title
plt.title("Salary by Employee", fontsize=16)
plt.xlabel("Employee Name", fontsize=12)
plt.ylabel("Salary ($)", fontsize=12)

# 3. Save and show
plt.savefig("day10/line_chart.png")
plt.show()

# 1. Create the scatter plot
plt.figure(figsize=(8, 5))
plt.scatter(df["id"], df["salary"], color="red", s=100) # s=100 makes the dots bigger

# 2. Add labels and title
plt.title("Salary Distribution by ID", fontsize=16)
plt.xlabel("Employee ID", fontsize=12)
plt.ylabel("Salary ($)", fontsize=12)
plt.grid(True)

# 3. Save and show
plt.savefig("day10/scatter_chart.png")
plt.show()