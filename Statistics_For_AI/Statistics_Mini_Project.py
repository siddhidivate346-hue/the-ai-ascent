import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("DATASET/FIFA_matches_dataset.csv")
home_score = data["home_score"]
home_shot = data["home_total_shots"]

print("="*45)
print("      FIFA MATCH STATISTICAL REPORT")
print("="*45)

print("\n ------ BASIC STATISTICS ------")
print("Total Matches :",len(home_score))
print("Mean :",home_score.mean())
print("Median :",home_score.median())
print("Mode :",home_score.mode()[0])

data_range = home_score.max() - home_score.min()
print("Range :",data_range)
print("variance :",home_score.var())
print("Standard Deviation :",home_score.std())

# QUARTILES & IQR

print("\n ----- QUARTILES ------")
Q1 = home_score.quantile(0.25)
Q2 = home_score.quantile(0.50)
Q3 = home_score.quantile(0.75)

print("Q1 :",Q1)
print("Q2 (median) :",Q2)
print("Q3 :",Q3)

IQR = Q3-Q1
print("IQR :", IQR)

# OUTLIERS

lower_limit = Q1 - 1.5 *IQR
upper_limit = Q3 + 1.5 *IQR
outliers = home_score[
    (home_score < lower_limit) | (home_score > upper_limit)
]
print("\n----- OUTLIERS -----")

if len(outliers) == 0:
    print("No Outliers Found")
else:
    print(outliers)

# ==============================
# CORRELATION
# ==============================

print("\n----- CORRELATION -----")
correlation = home_shot.corr(home_score)

print("columns compared :")
print("home_total_shots <----> home_score")
print("\n correlation value :",correlation)
if correlation > 0:
    print("Positive correlation")
elif correlation <0:
    print("Negative correlation")
else:
    print("No correlation")

#HISTOGRAM
plt.figure(figsize=(8,5))
plt.hist(home_score,bins= range(0,9))
plt.title("Distribution Of Home Goals")
plt.xlabel("Goals")
plt.ylabel("Number Of Matches")
plt.show()

#BOX PLOT

plt.figure(figsize=(6,5))
plt.boxplot(home_score)
plt.title("Box Plot Of Home Goals")
plt.ylabel("Goals")
plt.show()
print("\n Analysis Completed Successfully !")