class Car:
    def __init__(self, type):
        self.type = type

    color = "Black"
    @staticmethod
    def start():
        print("car started ....")

    @staticmethod
    def stop():
        print("car stopped...")
    

class ToyotaCar(Car):
    def __init__(self, name, type):
        self.name = name
        super().__init__(type)
        super().start()

car1 = ToyotaCar("Fortuner", "electric")
print(car1.type)