
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def get_balance(self):
        return self.balance

    def set_balance(self, balance):
        self.balance = balance

    def display(self):
        print("Account Holder:", self.name)
        print("Balance:", self.balance)


a1 = BankAccount("Ram", 5000)

print("Old Balance:", a1.get_balance())

a1.set_balance(8000)

print("New Balance:", a1.get_balance())