import numpy as np
import matplotlib.pyplot as plt

# Example dataset (temperature in °C and rainfall in mm)
temperature = np.array([30, 32, 31, 29, 28, 33, 34, 27, 26, 35])
rainfall = np.array([5, 3, 4, 7, 8, 2, 1, 9, 10, 0])

# Calculate correlation coefficient
correlation = np.corrcoef(temperature, rainfall)[0, 1]

print("Correlation coefficient between Temperature and Rainfall:", correlation)

# Scatter plot
plt.scatter(temperature, rainfall)
plt.xlabel("Temperature (°C)")
plt.ylabel("Rainfall (mm)")
plt.title("Temperature vs Rainfall Scatter Plot")
plt.show()