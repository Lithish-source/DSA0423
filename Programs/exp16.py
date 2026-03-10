import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score

# dataset
data = pd.DataFrame({
    "age":[45,50,36,60,48,33,55,42],
    "gender":["M","F","F","M","M","F","M","F"],
    "blood_pressure":[130,120,110,140,135,115,145,125],
    "cholesterol":[220,210,190,240,230,200,250,215],
    "outcome":["Good","Good","Bad","Bad","Good","Bad","Bad","Good"]
})

# encode data
le_gender = LabelEncoder()
data["gender"] = le_gender.fit_transform(data["gender"])

le_outcome = LabelEncoder()
data["outcome"] = le_outcome.fit_transform(data["outcome"])

# features and target
X = data[["age","gender","blood_pressure","cholesterol"]]
y = data["outcome"]

# split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2)

# train model
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# test accuracy
predictions = model.predict(X_test)
print("Model Accuracy:", accuracy_score(y_test, predictions))

# predict new patient
new_patient = [[40,1,128,210]]
result = model.predict(new_patient)

if result[0] == 1:
    print("Prediction: Good response to treatment")
else:
    print("Prediction: Bad response to treatment")