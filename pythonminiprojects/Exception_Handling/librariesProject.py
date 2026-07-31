import pandas as pd
import matplotlib.pyplot as plt
data={
"employee_id": [101,102,103,104,105,106,107,108,109,110],
    "name": ["Amit", "Priya", "Rahul", "Sneha", "Karan", "Neha", "Arjun", "Pooja", "Vikram", "Anjali"],
    "department": ["IT", "HR", "IT", "Finance", "IT", "HR", "Finance", "IT", "HR", "Finance"],
    "city": ["Pune ", " MUMBAI", "Delhi", "Bengluru ", "pune", "MUMBAI ", "delhi", " PUNE", "mumbai", "DELHI"],
    "salary": [60000, None, 75000, 50000, 80000, None, 65000, 72000, None, 58000],
    "performance_score": [4.5, 3.8, 4.2, None, 4.9, 3.5, None, 4.0, 3.9, None],
    "experience_years": [2,5,3,4,6,2,5,3,4,2]
}
df = pd.DataFrame(data)
print("--ORIGINAL DATA--",df)

avg = df["salary"].mean()
df["salary"]=df["salary"].fillna(avg)

df["name"]=df["name"].str.strip().str.lower()
df["department"]=df["department"].str.strip().str.lower()
df["city"]=df["city"].str.strip().str.lower()
print("\n -- CLEANED DATA--\n",df)

avg_salary=df["salary"].mean()
print("\n AVERAGE SALARY:", avg_salary)

max_salary=df["salary"].max()
top_salary=df[df["salary"]==max_salary]
print("\n HIGHEST SALARY:\n",top_salary)

highest_sal_emp=df[df["salary"]>10000]
print("\n highest salary emp with > 10000:",highest_sal_emp)

#VISUALIZATION

df=df.sort_values(by="salary")
plt.bar(df["name"],df["salary"],label="marks (Bar)")
plt.plot(df["name"],df["salary"],color="red",marker=0,label="marks(line)")

plt.xlabel("name")
plt.ylabel("salary")
plt.title("emp performance analysis")
plt.legend()
plt.show()

#save to csv

df.to_csv=("employee.csv")
print("\n csv file 'employee.csv' saved successfully!")
