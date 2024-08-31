class Student:

    # default Constructor
    def __init__(self):
        print("adding name to student list")

    # parameterized constructor
    def __init__(self, fullname, marks):
        print("adding name to student list")
        self.name = fullname
        self.marks = marks

    def welcome_student(self):
        print("Welcome Students !!")

s1 = Student("shahaji", 78)
print(s1.name, s1.marks)
s2 = Student("arun", 58)
print(s2.name, s2.marks)
s2.welcome_student()