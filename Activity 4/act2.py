import numpy as np

# Dataset
house_prices = np.array([2.5, 3.0, 2.8, 3.2, 15.0, 2.9, 3.1, 2.7, 100.0])

# 1. Identify Outliers using Z-score
from scipy.stats import zscore

z_scores = zscore(house_prices)
outliers = house_prices[np.abs(z_scores) > 3]

print("Outliers detected:", outliers)


# 2 & 3. Treatment

# Correct the data entry error
house_prices_corrected = np.where(house_prices == 100.0, 10.0, house_prices)

print("\nDataset after correcting typo:")
print(house_prices_corrected)

# Mansion value (15.0) is legitimate so we keep it
print("\n15.0 is kept because it represents a real mansion price.")