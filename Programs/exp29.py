import pandas as pd
import numpy as np
from scipy import stats

# Load dataset
df = pd.read_csv("customer_reviews.csv")

# Extract ratings
ratings = df["rating"]

# Sample statistics
n = len(ratings)
mean_rating = ratings.mean()
std_dev = ratings.std()

# Confidence level
confidence = 0.95

# Standard error
std_error = std_dev / np.sqrt(n)

# Z value
z = stats.norm.ppf((1 + confidence) / 2)

# Margin of error
margin = z * std_error

# Confidence interval
lower = mean_rating - margin
upper = mean_rating + margin

print("Average Rating:", mean_rating)
print("95% Confidence Interval:", (lower, upper))