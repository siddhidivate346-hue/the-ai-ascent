import pandas as pd
data=pd.read_csv("DATASET/student_Dataset.csv")

print("="*45)
print("      STUDENT DATASET")
print("="*45)

print("\nFIRST 5 ROWS")
print(data.head())

print("\nDATASET INFORMATION")
print(data.info())

print("\n MISSING VALUES")
print(data.isnull().sum())

#FILL MISSING VALUES
data["Age"] = data["Age"].fillna(data["Age"].mean())
data["Python_Score"] = data["Python_Score"].fillna(data["Python_Score"].mean())
data["AI_Score"] = data["AI_Score"].fillna(data["AI_Score"].mean())
data["Attendance"] = data["Attendance"].fillna(data["Attendance"].mean())

print("\nMissing Values After Filling")
print(data.duplicated().sum())
print("Rows After Removing Duplication :",len(data))

data= data.rename(columns={ "Python_score" : "python_marks"})
print("\nColumns")
data["Attendance"] = data["Attendance"].astype(int)
print("\nATTENDANCE DATA TYPE")
print(data["Attendance"].dtype)

# SAVE CLEAN DATASET
data.to_csv("DATASET/Student_Dataset_clean.csv",index=False)
print("\nClean Dataset Saved Successfully !!")