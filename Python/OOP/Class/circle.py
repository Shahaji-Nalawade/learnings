class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        # return 3.14 * self.radius ** 2
        return 22/7 * self.radius ** 2
    
    def perimeter(self):
        # return 2 * 3.14 * self.radius
        return 2 * 22/7 * self.radius

c1 = Circle(21)
print(c1.area())
print(c1.perimeter())