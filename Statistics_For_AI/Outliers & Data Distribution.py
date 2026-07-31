import pandas as pd
data = pd.read_csv("DATASET/FIFA_matches_dataset.csv")
home_score = data["home_score"]

print("==== HOME GOAL ANALYSIS =====")
print("MEAN GOALS:",home_score.mean())
print("MEDIAN GOALS:",home_score.median())

# OUTLIER DETECTION

Q1 = home_score.quantile(0.25)
Q3 = home_score.quantile(0.75)

IQR = Q3-Q1
lower_limit = Q1- 1.5*IQR
upper_limit = Q3+1.5*IQR

outliers = home_score[
    (home_score < lower_limit)
    | (home_score > upper_limit)
]

print("\n ===== OUTLIERS ======")
print(outliers)