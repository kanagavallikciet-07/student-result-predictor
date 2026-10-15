import numpy as np
import joblib
from sklearn.tree import DecisionTreeClassifier

X = np.array([
    [1, 40, 10],
    [2, 45, 15],
    [3, 50, 20],
    [4, 55, 25],
    [5, 60, 30],
    [6, 65, 35],
    [7, 70, 40],
    [1, 50, 20],
    [2, 60, 30],
    [3, 70, 40],
    [4, 75, 45],
    [5, 80, 55],
    [6, 85, 65],
    [7, 90, 75]
])

y = np.array([
    "Fail", "Fail", "Fail", "Fail",
    "Fail", "Pass", "Pass", "Fail",
    "Fail", "Fail", "Pass", "Pass",
    "Pass", "Pass"
])

model = DecisionTreeClassifier(random_state=42)
model.fit(X, y)

joblib.dump(model, "student_model.pkl")
print("Model trained successfully")
