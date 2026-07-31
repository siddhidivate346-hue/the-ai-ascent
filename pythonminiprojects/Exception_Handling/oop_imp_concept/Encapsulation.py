# pr code 1

"""class bankaccount:
    def __init__(self,name,balance):
        self.name = name
        self.__balance = balance

    def show_balance(self):
        print("balance:",self._balance)

    def deposite(self,amount):
        self._balance +=amount
        print("amount deposited:",amount)

account = bankaccount("siddhi",100000)
account.show_balance()
account.deposite(800)
account.show_balance()"""

# code 2
class techprofile:
    def __init__(self,name,role,salary):
        self.name = name
        self.role = role
        self.__salary = salary

    def show_profile(self):
        print("NAME :",self.name)
        print("ROLE :",self.role)

    def show_salary(self):
        print("SALARY:",self.__salary)

class AIEngineer(techprofile):
    def __init__(self,name,role,salary,skill):
        super().__init__(name,role,salary)
        self.skill = skill

    def show_skill(self):
        print("SKILL:",self.skill)

name = input("enter name: ")
role = input("enter your role: ")
salary = int(input("enter salary: "))
skill = input("enter your skill:")

p1 = AIEngineer(name,role,salary,skill)

print("\n ---profile details---")
p1.show_profile()
print("\n ---skill detailes---")
p1.show_skill()
print("\n ---salary details--- ")
p1.show_salary()


