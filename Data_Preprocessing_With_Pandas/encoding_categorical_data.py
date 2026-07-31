import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

data = pd.read_csv("DATASET/Student_Dataset.csv")

# CREATE DEPARTMENT COLUMN
departments = [
    "AI & DS","Computer", "IT","ENTC","Mechanical","Civil"
]
data["Departments"] = np.resize(departments, len(data))
print("=" * 50)
print("ORIGINAL DATA")
print("=" * 50)
print(data[["Departments", "City"]].head())

# LABEL ENCODING
encoder = LabelEncoder()
data["Department_Label"] = encoder.fit_transform(data["Departments"])
data["City_Label"] = encoder.fit_transform(data["City"])
print("\nLABEL ENCODING")

print(
    data[
        ["Departments","Department_Label","City","City_Label"
        ]
    ].head(10)
)

# ONE HOT ENCODING
one_hot = pd.get_dummies(
    data,
    columns=["Departments", "City"]
)
print("\nONE HOT ENCODING")
print(one_hot.head())

# COMPARISON
print("\nCOMPARISON")
print("\nLabel Encoding")
print("- Converts categories into one numeric column.")
print("- Uses less memory.")
print("- May create a false order.")
print("\nOne-Hot Encoding")
print("- Creates one column per category.")
print("- Uses only 0 and 1.")
print("- Better when categories have no natural order.")