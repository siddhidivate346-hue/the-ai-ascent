
 #SIMPLE CODE
"""class vehicle:
    def start(self):
        print("vehicle started")

class car(vehicle):
    def drive(self):
        print("car is driving")

c1 = car()
c1.start()
c1.drive()"""

# MINIPROJECT:

class Employee:
    def __init__(self, name, department):
        self.name = name
        self.department = department

    def show_employee(self):
        print("Name:", self.name)
        print("Department:", self.department)


class AIEngineer(Employee):
    def __init__(self, name, department, skill):
        super().__init__(name, department)
        self.skill = skill

    def show_skill(self):
        print("Skill:", self.skill)


# OBJECTS

e1 = AIEngineer("Siddhi", "AI", "Generative AI")
e2 = AIEngineer("Raj", "ML", "Computer Vision")

print("\n--- Employee 1 ---")
e1.show_employee()
e1.show_skill()

print("\n--- Employee 2 ---")
e2.show_employee()
e2.show_skill()