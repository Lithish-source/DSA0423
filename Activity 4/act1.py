import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import skew, kurtosis, zscore

normal_data = np.random.normal(loc=50, scale=5, size=1000)
skewed_data = np.random.exponential(scale=1, size=1000)

df = pd.DataFrame({
    "Normal_Data": normal_data,
    "Skewed_Data": skewed_data
})
plt.figure(figsize=(10,4))

plt.subplot(1,2,1)
sns.histplot(df["Normal_Data"], kde=True)
plt.title("Normal Distribution")

plt.subplot(1,2,2)
sns.histplot(df["Skewed_Data"], kde=True)
plt.title("Exponential (Skewed) Distribution")

plt.show()

print("Skewness:")

print("Normal Data:", skew(normal_data))
print("Skewed Data:", skew(skewed_data))

print("\nKurtosis (Fisher's Definition - Excess Kurtosis):")

print("Normal Data:", kurtosis(normal_data))
print("Skewed Data:", kurtosis(skewed_data))


z_scores = zscore(skewed_data)

outliers = skewed_data[np.abs(z_scores) > 3]

print("\nNumber of outliers in skewed_data:", len(outliers))
