"""import pandas as pd
import matplotlib.pyplot as plt
data={
    "name":["A","B","C","D","E"],
    "marks":[80,70,90,75,94],
    "city":["pune","pune","mumbai","mumbai","pune"]
}

df=pd.DataFrame(data)
result = df.groupby("city")["marks"].mean()
print(result)

sorted_df = df.sort_values(by="marks",ascending=False)
print(sorted_df)

filtered=df[(df["marks"]>80) & (df["city"]=="pune")]
print(filtered)

plt.bar(df["name"],df["marks"],label="marks")
plt.plot(df["name"],df["marks"],marker="o",color="red")
plt.xlabel("student")
plt.ylabel("marks")
plt.title("student performance")
plt.legend()
plt.show()"""
import pandas as pd
import matplotlib.pyplot as plt

# 🔹 Dataset
data = {
    "name": ["A", "B", "C", "D", "E"],
    "marks": [80, 70, 90, 75, 94],
    "city": ["pune", "pune", "mumbai", "mumbai", "pune"]
}

df = pd.DataFrame(data)

# 🔹 1️⃣ Category Analysis (Group By)
result = df.groupby("city")["marks"].mean()
print("\n📊 Average Marks by City:\n", result)

# 🔹 2️⃣ Sorting
sorted_df = df.sort_values(by="marks", ascending=False)
print("\n📈 Sorted Data (Top Performers First):\n", sorted_df)

# 🔹 3️⃣ Multiple Filtering
filtered = df[(df["marks"] > 80) & (df["city"] == "pune")]
print("\n🔥 Students with marks > 80 from Pune:\n", filtered)

# 🔹 4️⃣ Visualization

# Optional: sort before plotting for better view
df = df.sort_values(by="marks")

plt.bar(df["name"], df["marks"], label="Marks (Bar)")
plt.plot(df["name"], df["marks"], marker="o", color="red", label="Marks (Line)")

plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Student Performance Analysis")

plt.legend()
plt.show()