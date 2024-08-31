class Account:
    def __init__(self, acc, pwd):
        self.acc = acc 
        # __ is used to make attribute as private attribute
        self.__pwd = pwd

    def reset_pass(self):
        print(self.__pwd)


acc1 = Account("12345", "abcd")

print(acc1.acc)
# print(acc1.__pwd)
acc1.reset_pass()