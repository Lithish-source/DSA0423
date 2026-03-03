import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

temperature = [22, 24, 28, 32, 35, 36, 34, 33, 31, 29, 25, 23]
rainfall = [15, 20, 25, 40, 60, 120, 150, 130, 100, 70, 30, 20]

# Line Plot for Temperature
plt.figure()
plt.plot(months, temperature, marker='o')
plt.title("Monthly Temperature - Line Plot")
plt.xlabel("Month")
plt.ylabel("Temperature (°C)")
plt.show()

# Scatter Plot for Rainfall
plt.figure()
plt.scatter(months, rainfall)
plt.title("Monthly Rainfall - Scatter Plot")
plt.xlabel("Month")
plt.ylabel("Rainfall (mm)")
plt.show()