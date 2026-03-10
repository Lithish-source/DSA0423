import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample car dataset
data = {
    "Car": ["A","B","C","D","E","F","G","H"],
    "Horsepower": [130,165,150,140,198,220,215,225],
    "Mileage": [18,15,18,16,14,14,15,14],
    "Weight": [3504,3693,3436,3433,4341,4354,4312,4425],
    "Price": [20000,25000,22000,21000,32000,35000,34000,36000]
}

df = pd.DataFrame(data)

# ---- Multivariate Scatter Plot ----
plt.scatter(df["Horsepower"], df["Mileage"], s=df["Weight"]/20)
plt.xlabel("Horsepower")
plt.ylabel("Mileage")
plt.title("Multivariate Scatter Plot (Horsepower vs Mileage)")
plt.show()

# ---- Scatter Plot Matrix ----
sns.pairplot(df[["Horsepower","Mileage","Weight","Price"]])
plt.show()