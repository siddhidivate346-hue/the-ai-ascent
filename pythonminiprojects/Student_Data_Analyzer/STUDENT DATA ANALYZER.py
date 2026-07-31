import pandas as pd
import matplotlib.pyplot as ptl

data={
"student_id": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],

    "name": [
        "Amit", "Neha", "Raj", "Pooja", "Karan",
        "Sneha", "Arjun", "Riya", "Vikram", "Anjali"],

    "marks": [ 78, None, 92, 65, 88,
        None, 55, 73, 95, None ],

    "city": [
        "Pune ", " MUMBAI", "delhi", "Pune", "DELHI",
        "mumbai ", "Bengluru", " pune", "DELHI ", "Mumbai"],

    "course": [
        "AI", "Data Science", "Web Dev", "AI", "Cyber Security",
        "Data Science", "AI", "Web Dev", "Cyber Security", "AI"],

    "attendance": [
        85, 90, 95, 70, 88,
        76, 60, 82, 98, 79]
}
df = pd.DataFrame(data)
df.to_csv("students.csv" ,index= False)
print("student.csv created successfully")

try:
    df=pd.read_csv("students.csv")
    print("csv loaded successfully!\n")
    print(df)
except FileNotFoundError:
    print("file not found!")

avg_marks = df["marks"].mean()
df["marks"] = df["marks"].fillna(avg_marks)
df["city"] = df["city"].str.strip().str.lower()
df["name"]=df["name"].str.strip().str.lower()
print("\n CLEANED DATA:\n")
print(df)

average = df["marks"].mean()
print("\n AVERAGE MARKS:",average)

highest = df["marks"].max()
top_student = df[df["marks"]==highest]
print("\n HIGHEST SCORER :\n")
print(top_student)

city_avg=df.groupby("city")["marks"].mean()
print("\n CITY-WISE AVERAGE:\n")
print(city_avg)

try:
    minimum = int(input("enter minimum marks:"))
    filtered = df[df["marks"]>minimum]
    print(filtered)
except ValueError:
    print("please enter valid number!")

ptl.bar(df["name"],df["marks"])
ptl.xlabel("students")
ptl.ylabel("marks")
ptl.title("student performance")
ptl.show()