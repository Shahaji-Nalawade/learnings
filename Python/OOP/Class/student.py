class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("hi " + self.name , "your average score is :", sum/3 )

    @staticmethod
    def hello():
        print("Hello")

s1 = Student("tony stark", [99,98,92])
s1.get_avg()
s1.hello()