import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score

# Example dataset
data = pd.DataFrame({
    "age": [25, 40, 35, 28, 50, 45, 30, 38],
    "income": [40000, 80000, 60000, 45000, 90000, 75000, 50000, 65000],
    "browsing_duration": [10, 20, 15, 8, 25, 18, 12, 16],
    "device_type": ["mobile", "desktop", "tablet", "mobile", "desktop", "tablet", "mobile", "desktop"],
    "purchase": ["Yes", "No", "Yes", "No", "Yes", "No", "Yes", "No"]
})

# Encode categorical variables
le_device = LabelEncoder()
data["device_type"] = le_device.fit_transform(data["device_type"])

le_purchase = LabelEncoder()
data["purchase"] = le_purchase.fit_transform(data["purchase"])

# Features and target
X = data[["age", "income", "browsing_duration", "device_type"]]
y = data["purchase"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train decision tree classifier
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# Evaluate model
pred = model.predict(X_test)
print("Model Accuracy:", accuracy_score(y_test, pred))

# Predict for a new customer
new_customer = pd.DataFrame({
    "age": [32],
    "income": [55000],
    "browsing_duration": [14],
    "device_type": [le_device.transform(["mobile"])[0]]
})

prediction = model.predict(new_customer)

if prediction[0] == 1:
    print("Prediction: Customer likely to make a purchase")
else:
    print("Prediction: Customer unlikely to make a purchase")