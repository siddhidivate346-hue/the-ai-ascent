import pandas as pd
import numpy as np

# Read Dataset
data = pd.read_csv("DATASET/Student_Dataset.csv")

# Create Department Column
departments = ["AI & DS", "Computer", "IT", "ENTC", "Mechanical", "Civil"]
data["Department"] = np.resize(departments, len(data))

# Fill missing values
data["Python_Score"] = data["Python_Score"].fillna(0)
data["AI_Score"] = data["AI_Score"].fillna(0)

# ======================================
# NEW COLUMNS
# ======================================

# Total Marks
data["Total_Marks"] = data["Python_Score"] + data["AI_Score"]

# Average Marks
data["Average_Marks"] = data["Total_Marks"] / 2

# Grade
grades = []

for avg in data["Average_Marks"]:

    if avg >= 90:
        grades.append("A")

    elif avg >= 75:
        grades.append("B")

    elif avg >= 60:
        grades.append("C")

    elif avg >= 40:
        grades.append("D")

    else:
        grades.append("F")

data["Grade"] = grades

# Pass / Fail
status = []

for avg in data["Average_Marks"]:

    if avg >= 40:
        status.append("Pass")
    else:
        status.append("Fail")

data["Pass_Fail"] = status

# Scholarship
scholarship = []

for avg in data["Average_Marks"]:

    if avg >= 85:
        scholarship.append("Eligible")
    else:
        scholarship.append("Not Eligible")

data["Scholarship"] = scholarship

# ======================================
# DISPLAY RESULT
# ======================================

print("=" * 70)
print("          STUDENT PERFORMANCE REPORT")
print("=" * 70)

print(data[
    [
        "Student_ID",
        "Name",
        "Department",
        "Python_Score",
        "AI_Score",
        "Total_Marks",
        "Average_Marks",
        "Grade",
        "Pass_Fail",
        "Scholarship"
    ]
])

print("\nReport Generated Successfully!")