class Account:
    def __init__(self, balance, acc):
        self.balance = balance
        self.acc = acc
    
    # debit method
    def debit(self, amount):
        self.balance -= amount
        print("Rs. ", amount, "was debited")
        print("Total balance =", self.get_balance())
    
    # credit method
    def credit(self, amount):
        self.balance += amount
        print("Rs. ", amount, "was credited")
        print("Total balance =", self.get_balance())


    def get_balance(self):
        return self.balance

acc1 = Account(10000, 12345)
print("account balance is ", acc1.get_balance())
acc1.debit(1000)
acc1.credit(500)
acc1.credit(20000)
acc1.debit(5000)

