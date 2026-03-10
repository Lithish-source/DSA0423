import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score

# Example dataset
data = pd.DataFrame({
    "weight": [150, 170, 140, 130, 180, 160],
    "color": ["red", "orange", "yellow", "yellow", "orange", "red"],
    "texture": ["smooth", "rough", "smooth", "smooth", "rough", "smooth"],
    "type": ["apple", "orange", "banana", "banana", "orange", "apple"]
})

# Encode categorical columns
le_color = LabelEncoder()
data["color"] = le_color.fit_transform(data["color"])

le_texture = LabelEncoder()
data["texture"] = le_texture.fit_transform(data["texture"])

le_type = LabelEncoder()
data["type"] = le_type.fit_transform(data["type"])

# Features and target
X = data[["weight", "color", "texture"]]
y = data["type"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Create kNN model
k = 3
model = KNeighborsClassifier(n_neighbors=k)
model.fit(X_train, y_train)

# Evaluate accuracy
pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, pred))

# Predict unknown fruit
unknown_fruit = [[160, le_color.transform(["orange"])[0], le_texture.transform(["rough"])[0]]]
prediction = model.predict(unknown_fruit)

print("Predicted fruit type:", le_type.inverse_transform(prediction))	