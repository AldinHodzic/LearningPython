

class Account:
    
    id = 0

    def __init__(self, name):
        self.ID = Account.id
        Account.id += 1
        self.balance = 0
        self.owner = name

    def _deposit(self, cash):
        self.balance += cash

    def _withdraw(self, cash):
        self.balance -= cash

    def _balance(self):
        print(f"Current balance is: {self.balance}")

acc1 = Account("Aldin")

print(f"Name: {acc1.owner}")
acc1._balance()
acc1._deposit(200)
acc1._balance()
