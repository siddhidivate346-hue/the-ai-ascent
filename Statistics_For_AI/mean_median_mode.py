import numpy as np
from statistics import mode

marks = []
for i in range(5):
    mark = int(input(f" ENTER MARKS {i+1}: "))
    marks.append(mark)

mean_marks = np.mean(marks)
median_marks = np.median(marks)
mode_marks = mode(marks)

highest_mark = max(marks)
lowest_mark = min(marks)

print("\n ==== STUDENT PERFORMANCE REPORT ====")

print("MARKS: ",marks)
print("MEAN:",mean_marks)
print("MEDIAN:",median_marks)
print("MOD:",mode_marks)
print("HIGHEST_MARK:",highest_mark)
print("LOWEST_MARK:",lowest_mark)