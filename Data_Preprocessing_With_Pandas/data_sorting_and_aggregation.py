import pandas as pd
import numpy as np
# Read Dataset
data = pd.read_csv("DATASET/Student_Dataset.csv")

# Create Department Column
departments = ["AI & DS", "Computer", "IT", "ENTC", "Mechanical", "Civil"]
data["Department"] = np.resize(departments, len(data))

print("=" * 50)
print("     SORTING & GROUPBY ANALYSIS")
print("=" * 50)

# =====================================
# PART A : SORTING
# =====================================

print("\nTOP 5 STUDENTS BY PYTHON SCORE")
top_students = data.sort_values(by="Python_Score", ascending=False)
print(top_students[["Name", "Department", "Python_Score"]].head())

print("\nBOTTOM 5 STUDENTS BY ATTENDANCE")
bottom_students = data.sort_values(by="Attendance", ascending=True)
print(bottom_students[["Name", "Department", "Attendance"]].head())

# =====================================
# PART B : GROUPBY
# =====================================

print("\nAVERAGE PYTHON SCORE BY DEPARTMENT")
print(data.groupby("Department")["Python_Score"].mean())
print("\nAVERAGE ATTENDANCE BY DEPARTMENT")
print(data.groupby("Department")["Attendance"].mean())
print("\nHIGHEST PYTHON SCORE IN EACH DEPARTMENT")
print(data.groupby("Department")["Python_Score"].max())
print("\nNUMBER OF STUDENTS IN EACH DEPARTMENT")
print(data.groupby("Department")["Student_ID"].count())




