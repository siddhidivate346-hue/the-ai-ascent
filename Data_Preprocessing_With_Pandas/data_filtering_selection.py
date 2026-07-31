import pandas as pd

# Read Dataset
data = pd.read_csv("DATASET/Student_Dataset.csv")

print("=" * 45)
print("      FILTERING & SELECTING DATA")
print("=" * 45)

# Select One Column
print("\nStudent Names")
print(data["Name"])

# Select Multiple Columns
print("\nName and City")
print(data[["Name", "City"]])

# Filter Students from Pune
print("\nStudents from Pune")
print(data[data["City"] == "Pune"])

# Filter Python Score Greater Than 90
print("\nPython Score > 90")
print(data[data["Python_Score"] > 90])

# Filter Study Hours Greater Than 5
print("\nStudy Hours > 5")
print(data[data["Study_Hours"] > 5])

# Multiple Conditions
print("\nPune Students with Python Score > 85")

result = data[
    (data["City"] == "Pune") &
    (data["Python_Score"] > 85)
]

print(result)