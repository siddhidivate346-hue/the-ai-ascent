class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.__salary = salary

    def show_details(self):
        print("ID:", self.emp_id)
        print("Name:", self.name)

    def show_salary(self):
        print("Salary:", self.__salary)


class AIResearcher(Employee):
    def __init__(self, emp_id, name, salary, research_area):
        super().__init__(emp_id, name, salary)
        self.research_area = research_area

    def work(self):
        print("Training AI Models")


class DataScientist(Employee):
    def __init__(self, emp_id, name, salary, tool):
        super().__init__(emp_id, name, salary)
        self.tool = tool

    def work(self):
        print("Analyzing Datasets")


class MLOpsEngineer(Employee):
    def __init__(self, emp_id, name, salary, platform):
        super().__init__(emp_id, name, salary)
        self.platform = platform

    def work(self):
        print("Deploying ML Systems")


employees = []

file = open("employees.csv", "w")

file.write("ID,Name,Role,Salary,Specialization\n")

for i in range(3):

    print("\n===== Employee", i + 1, "=====")

    print("1. AI Researcher")
    print("2. Data Scientist")
    print("3. MLOps Engineer")

    choice = int(input("Enter Choice: "))

    emp_id = input("Enter Employee ID: ")
    name = input("Enter Name: ")
    salary = int(input("Enter Salary: "))

    if choice == 1:

        research_area = input("Enter Research Area: ")

        emp = AIResearcher(
            emp_id,
            name,
            salary,
            research_area
        )

        file.write(
            f"{emp_id},{name},AI Researcher,{salary},{research_area}\n"
        )

    elif choice == 2:

        tool = input("Enter Tool: ")

        emp = DataScientist(
            emp_id,
            name,
            salary,
            tool
        )

        file.write(
            f"{emp_id},{name},Data Scientist,{salary},{tool}\n"
        )

    elif choice == 3:

        platform = input("Enter Platform: ")

        emp = MLOpsEngineer(
            emp_id,
            name,
            salary,
            platform
        )

        file.write(
            f"{emp_id},{name},MLOps Engineer,{salary},{platform}\n"
        )

    else:
        print("Invalid Choice")
        continue

    employees.append(emp)

file.close()

print("\n===== EMPLOYEE REPORT =====")

for emp in employees:

    emp.show_details()
    emp.show_salary()
    emp.work()

    print("----------------------")

print("\nEmployee data saved in employees.csv")

print("\n===== STORED CSV DATA =====")

with open("employees.csv", "r") as file:
    print(file.read())