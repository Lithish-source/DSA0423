import numpy as np
from scipy import stats

# Example sample revenue data (100 customers)
revenue = np.random.normal(500, 50, 100)   # mean ≈ 500, std ≈ 50

# Sample size
n = len(revenue)

# Sample mean and standard deviation
mean_revenue = np.mean(revenue)
std_dev = np.std(revenue, ddof=1)

# Confidence level
confidence = 0.95

# Standard error
std_error = std_dev / np.sqrt(n)

# Calculate confidence interval
z = stats.norm.ppf((1 + confidence) / 2)
margin_error = z * std_error

lower = mean_revenue - margin_error
upper = mean_revenue + margin_error

print("Sample Mean Revenue:", mean_revenue)
print("95% Confidence Interval: ({:.2f}, {:.2f})".format(lower, upper))