import pandas as pd
data = pd.read_csv("DATASET/FIFA_matches_dataset.csv")
attendance = data["attendance"]
attendance = attendance.str.replace(",","")
attendance = attendance.astype(int)
print("\n ==== FIFA ATTENDANCE REPORT ====")

print("MEAN:",attendance.mean())
print("MEDIAN:",attendance.median())
print("RANGE :",attendance.max()-attendance.min())
print("VARIANCE:",attendance.var())
print("STANDARD_DEVIATION:",attendance.std())
print("HIGHEST ATTENDANCE:",attendance.max())
print("LOWEST ATTENDANCE:",attendance.min())
