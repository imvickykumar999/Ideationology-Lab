class Bank_Account:

    def __init__(self, balance = 0):
        self.balance = balance
        print("Hello!!! Welcome to the Deposit & Withdrawal Machine")

    def deposit(self, amount):
        # amount=float(input("Enter amount to be Deposited: "))
        self.balance += amount
        print("\n Amount Deposited:", amount)

    def withdraw(self, amount):
        # amount = float(input("Enter amount to be Withdrawn: "))

        if self.balance>=amount:
            self.balance-=amount
            print("\n You Withdrew:", amount)
        else:
            print("\n Insufficient balance ")

    def display(self):
        print("\n Net Available Balance=", self.balance)
