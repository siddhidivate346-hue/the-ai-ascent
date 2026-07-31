import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler
data = pd.read_csv("DATASET/Student_Dataset.csv")
print("=" * 50)
print("        FEATURE SCALING")
print("=" * 50)

# Select numerical columns
features = data[
    ["Age", "Study_Hours", "Python_Score", "AI_Score"]]
print("\nORIGINAL DATA")
print(features.head(10))

# STANDARDIZATION
standard_scaler = StandardScaler()

standard_scaled = standard_scaler.fit_transform(features)
standard_data = pd.DataFrame(standard_scaled,columns=features.columns
)
print("\nSTANDARD SCALING")
print(standard_data.head(10))

# NORMALIZATION
minmax_scaler = MinMaxScaler()
minmax_scaled = minmax_scaler.fit_transform(features)
minmax_data = pd.DataFrame(minmax_scaled,columns=features.columns)
print("\nMIN-MAX SCALING")
print(minmax_data.head(10))

# COMPARISON
print("\nCOMPARISON")
print("1. StandardScaler changes values around an average of 0.")
print("2. MinMaxScaler changes values into a range of 0 to 1.")
print("3. Both methods make different features more comparable.")

















