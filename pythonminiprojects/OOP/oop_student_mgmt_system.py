class Student:
    def __init__(self,name,marks,city):
        self.name = name
        self.marks = marks
        self.city = city
    def show_details(self):
        print("NAME:",self.name)
        print("MARKS:",self.marks)
        print("CITY:",self.city)

    def result(self):
        if self.marks >=40:
            print("RESULT:PASS")
        else:
            print("RESULT:FAIL")
    def grade(self):
        if self.marks>=90:
            print("Grade:A")
        elif self.marks>=75:
            print("Grade:B")
        elif self.marks>=50:
            print("Grade:C")
        else:
            print("Grade:D")

s1 = Student("rahul",86,"mumbai")
s2 = Student("asha",92,"pune")
s3 = Student("ravi",36,"delhi")

print("\n--STUDENT 1--")
s1.show_details()
s1.result()
s1.grade()

print("\n--STUDENT 2--")
s2.show_details()
s2.result()
s2.grade()

print("\n--- Student 3 ---")
s3.show_details()
s3.result()
s3.grade()
