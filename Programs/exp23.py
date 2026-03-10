import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score

# Example dataset
data = pd.DataFrame({
    "income": [30000, 50000, 70000, 40000, 90000, 60000, 45000, 80000],
    "credit_score": [600, 750, 720, 650, 800, 710, 680, 770],
    "debt_to_income": [35, 20, 25, 40, 18, 28, 32, 22],
    "employment_duration": [2, 5, 6, 3, 8, 4, 3, 7],
    "risk": ["High", "Low", "Low", "High", "Low", "Low", "High", "Low"]
})

# Encode target variable
le = LabelEncoder()
data["risk"] = le.fit_transform(data["risk"])

# Features and target
X = data[["income", "credit_score", "debt_to_income", "employment_duration"]]
y = data["risk"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# CART model (Decision Tree with Gini index)
model = DecisionTreeClassifier(criterion="gini")
model.fit(X_train, y_train)

# Evaluate model
predictions = model.predict(X_test)
print("Model Accuracy:", accuracy_score(y_test, predictions))

# Predict risk for a new applicant
new_applicant = pd.DataFrame({
    "income": [55000],
    "credit_score": [690],
    "debt_to_income": [30],
    "employment_duration": [4]
})

result = model.predict(new_applicant)

print("Predicted Risk Level:", le.inverse_transform(result)[0])