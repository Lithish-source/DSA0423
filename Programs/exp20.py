import pandas as pd
import matplotlib.pyplot as plt

# Read CSV file
df = pd.read_csv("players.csv")

# Top 5 players with highest goals
top_goals = df.nlargest(5, "goals")
print("Top 5 Players with Highest Goals:")
print(top_goals[["name", "goals"]])

# Top 5 players with highest salary
top_salary = df.nlargest(5, "salary")
print("\nTop 5 Players with Highest Salaries:")
print(top_salary[["name", "salary"]])

# Calculate average age
avg_age = df["age"].mean()
print("\nAverage Age of Players:", avg_age)

# Players above average age
above_avg = df[df["age"] > avg_age]
print("\nPlayers Above Average Age:")
print(above_avg["name"])

# Count players by position
position_count = df["position"].value_counts()

# Plot bar chart
plt.bar(position_count.index, position_count.values)
plt.xlabel("Position")
plt.ylabel("Number of Players")
plt.title("Distribution of Players by Position")
plt.show()