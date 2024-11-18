
class BalanceException(Exception):
    pass


class BankAccount:
    def __init__(self, initialamount, acctname):
        self.balance = initialamount
        self.name = acctname
        print(f"\nAccount '{self.name}'created.\nBalance: = $ {
              self.balance:.2f}")

    def getBalance(self):
        print(f"\nAccount '{self.name}' balance is $ {self.balance:.2f}")

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Deposited complete.")
        self.getBalance()

    def viableTransaxtion(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(f"\nSorry account '{self.name}' only has balance of $ {
                                   self.balance:.2f}")  # and not enough to withdraw $ {amount:.2f}

    def withdraw(self, amount):
        try:
            self.viableTransaxtion(amount)
            self.balance = self.balance - amount
            print("\nWithdrawal complete.")
            self.getBalance()
        except BalanceException as error:
            print(f'\nWithdrawal failed: {error}')

    def transfer(self, amount, otheracct):

        try:
            print('\n***********\n\nBank Transfer.. 🚀🚀 ')
            self.viableTransaxtion(amount)
            self.withdraw(amount)
            otheracct.deposit(amount)
            print("\nTransfer complete ✅✅ \n\n***********.")
        except BalanceException as error:
            print(f'\nTransfer interrupted. ❌❌: {error}')


class IntrestRewardsAcct(BankAccount):
    def deposit(self, amount):
        self.balance = self.balance + (amount * 1.05)
        print("\nDeposited complete.")
        self.getBalance()


class SavingsAcct(IntrestRewardsAcct):
  def __init__(self, initialamount, acctname):
    super().__init__(initialamount, acctname)
    self.fee = 5
    
  def withdraw(self, amount):
      try :
        self.viableTransaxtion(amount + self.fee)  
        self.balance = self.balance - (amount + self.fee)
        self.getBalance()
      except BalanceException as error:
        print(f'\nWithdrawal failed: {error}')  
