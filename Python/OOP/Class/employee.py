class Employee:
    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary
    
    def showDetails(self):
        print("role =", self.role)
        print("salary =", self.salary)
        print("department =", self.dept)

class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Engineer", "IT", "75000")

# e1 = Employee('accountant', "finance", "40000")
# e1.showDetails()

engg1 = Engineer('Elon Muck', "40")
engg1.showDetails()
