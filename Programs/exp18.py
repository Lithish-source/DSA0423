import pandas as pd

# Example dataset (daily temperatures for different cities)
data = {
    "City": ["Chennai","Chennai","Chennai","Delhi","Delhi","Delhi","Mumbai","Mumbai","Mumbai"],
    "Temperature": [32, 34, 31, 28, 30, 35, 29, 31, 30]
}

df = pd.DataFrame(data)

# 1. Mean temperature for each city
mean_temp = df.groupby("City")["Temperature"].mean()
print("Mean Temperature for each city:")
print(mean_temp)

# 2. Standard deviation of temperature for each city
std_temp = df.groupby("City")["Temperature"].std()
print("\nStandard Deviation for each city:")
print(std_temp)

# 3. City with highest temperature range
temp_range = df.groupby("City")["Temperature"].max() - df.groupby("City")["Temperature"].min()
city_highest_range = temp_range.idxmax()

print("\nTemperature Range for each city:")
print(temp_range)
print("City with highest temperature range:", city_highest_range)

# 4. City with most consistent temperature (lowest std deviation)
most_consistent_city = std_temp.idxmin()

print("\nCity with most consistent temperature:", most_consistent_city)