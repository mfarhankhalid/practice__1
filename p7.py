class InsufficientFundsError(Exception):
    pass

class BankAccount:
    def  __init__(self,owner,balance):
       self.owner=owner
       self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
    def withdraw(self,amount):
        if amount>self.balance:
            raise InsufficientFundsError(f"Cannot withdraw {amount}: balance is \n{self.balance}")
        self.balance-=amount


acount=BankAccount("Farhan",1000)
acount.deposit(500)
acount.withdraw(300)
print(acount.balance)


try:
   acount.withdraw(5000)
except InsufficientFundsError as e:
    print("Error:", e)