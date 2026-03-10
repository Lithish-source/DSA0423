import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Example dataset
data = pd.DataFrame({
    "customer_id": [1,2,3,4,5,6,7,8],
    "amount_spent": [200,500,150,800,120,700,300,650],
    "visit_frequency": [5,10,3,15,2,14,6,12]
})

# Features used for clustering
X = data[["amount_spent", "visit_frequency"]]

# Apply K-Means clustering
kmeans = KMeans(n_clusters=3, random_state=0)
data["cluster"] = kmeans.fit_predict(X)

print(data)

# Visualization of clusters
plt.scatter(data["amount_spent"], data["visit_frequency"], c=data["cluster"])
plt.xlabel("Amount Spent")
plt.ylabel("Visit Frequency")
plt.title("Customer Segmentation using K-Means")
plt.show()