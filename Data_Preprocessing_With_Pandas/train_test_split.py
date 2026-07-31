import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

data = pd.read_csv("DATASET/Student_Dataset_clean.csv")
print("*"*50)
print("   STUDENT SUPPORT PREDICTION ")
print("*"*50)

data["Academic_Support"]=np.where(
    data["Python_Score"]<60,
    "yes",
    "no")
print(data[["Python_Score","Academic_Support"]].head())

X=data[[
    "Age",
    "Study_Hours",
    "AI_Score"]]
Y = data["Academic_Support"]
X_train,X_test,Y_train,Y_test = train_test_split(
    X,
    Y,
    test_size=0.2,
    random_state =42
)
print("\n Original Dataset:",len(data))
print("Training Data :",len(X_train))
print("Testing Data :",len(X_test))

model = DecisionTreeClassifier()
model.fit(X_train,Y_train)
prediction = model.predict(X_test)
print(prediction)

accuracy = accuracy_score(Y_test,prediction)
print("\nAccuracy:",accuracy)






