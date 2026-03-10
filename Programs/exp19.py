import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Example dataset
data = pd.DataFrame({
    "customer_id": [1,2,3,4,5,6,7,8,9,10],
    "amount_spent": [200,500,150,800,120,700,300,650,400,250],
    "items_purchased": [5,10,3,15,2,14,6,12,8,4]
})

# Select features for clustering
X = data[["amount_spent","items_purchased"]]

# Apply K-Means clustering
kmeans = KMeans(n_clusters=3, random_state=0)
data["cluster"] = kmeans.fit_predict(X)

print("Customer Clusters:")
print(data)

# Plot clusters
plt.scatter(data["amount_spent"], data["items_purchased"], c=data["cluster"])

# Plot cluster centers
centers = kmeans.cluster_centers_
plt.scatter(centers[:,0], centers[:,1], marker='X', s=200)

plt.xlabel("Amount Spent")
plt.ylabel("Items Purchased")
plt.title("Customer Segmentation using K-Means Clustering")
plt.show()