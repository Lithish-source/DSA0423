import numpy as np
import pandas as pd

# Example dataset (population data)
data = [45, 50, 55, 60, 65, 70, 75, 80, 85, 90]

df = pd.DataFrame(data, columns=["values"])

# ----- Sampling Technique (Random Sampling) -----
sample = df.sample(n=5, random_state=1)

print("Sample Data:")
print(sample)

# ----- Mean Estimation -----
sample_mean = sample["values"].mean()
print("\nEstimated Mean from Sample:", sample_mean)

# ----- Variance Estimation -----
sample_variance = sample["values"].var()
print("Estimated Variance from Sample:", sample_variance)

# ----- Population statistics (for comparison) -----
population_mean = df["values"].mean()
population_variance = df["values"].var()

print("\nActual Population Mean:", population_mean)
print("Actual Population Variance:", population_variance)