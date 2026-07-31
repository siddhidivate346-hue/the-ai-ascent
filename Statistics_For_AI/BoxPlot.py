import pandas as pd
import matplotlib.pyplot as plt

data =pd.read_csv("DATASET/FIFA_matches_dataset.csv")
home_score = data["home_score"]
plt.figure(figsize=(7,5))
plt.boxplot(home_score)

plt.title("BOX PLOT OF HOME GOALS")
plt.ylabel("GOALS SCORED")

plt.show()









