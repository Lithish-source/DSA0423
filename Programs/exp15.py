import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Example clinical trial data
# (e.g., improvement scores or recovery measurements)

control_group = np.array([50, 52, 48, 47, 49, 51, 50, 46])
treatment_group = np.array([55, 58, 60, 57, 59, 61, 56, 58])

# Calculate means
control_mean = np.mean(control_group)
treatment_mean = np.mean(treatment_group)

# Perform independent t-test
t_stat, p_value = stats.ttest_ind(treatment_group, control_group)

print("Control Group Mean:", control_mean)
print("Treatment Group Mean:", treatment_mean)
print("T-statistic:", t_stat)
print("P-value:", p_value)

# Plot comparison using bar chart
groups = ['Control', 'Treatment']
means = [control_mean, treatment_mean]

plt.bar(groups, means)
plt.ylabel("Average Outcome")
plt.title("Treatment vs Control Group")

# Display p-value on graph
plt.text(0.5, max(means), f"p-value = {p_value:.4f}", ha='center')

plt.show()