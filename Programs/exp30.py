import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
data = pd.read_csv("shoe_sales.csv")

# Calculate frequency distribution
frequency = data.groupby("shoe_size")["quantity"].sum()

# Display frequency table
print("Frequency Distribution of Shoe Sizes:")
print(frequency)

# Plot bar chart
plt.bar(frequency.index, frequency.values)

plt.xlabel("Shoe Size")
plt.ylabel("Quantity Sold")
plt.title("Frequency Distribution of Shoe Sizes Sold")

plt.show()