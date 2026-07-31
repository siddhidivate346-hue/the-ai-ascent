import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("DATASET/FIFA_matches_dataset.csv")

home_score = data["home_score"]
plt.hist(home_score,bins=range(0,9))

plt.hist(home_score)

plt.title("DISTRIBUTION OF HOME GOALS")
plt.xlabel("Goals Scored")
plt.ylabel("Number Of Matches")

plt.show()
