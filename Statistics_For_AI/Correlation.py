import pandas as pd
data = pd.read_csv("DATASET/FIFA_matches_dataset.csv")

home_total_shots = data["home_total_shots"]
home_score = data["home_score"]

correlation = home_total_shots.corr(home_score)

print("==== FIFA CORRELATION REPORT ====")
print(data[["home_total_shots", "home_score"]].head(20))
print("correlation value:",correlation)

if correlation > 0:
    print("positive correlation")
    print("Teams with more shots tend to score more goals.")
elif correlation < 0:
    print("negative correlation")
else:
    print("no correlation")


    