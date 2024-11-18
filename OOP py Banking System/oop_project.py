from bank_account import*

Soultane = BankAccount(1000, "Soultane")
L3obi = BankAccount(2000, "l3obi")

Soultane.getBalance()
L3obi.getBalance()


L3obi.deposit(1000)

Soultane.withdraw(100000)
Soultane.withdraw(100)

Soultane.transfer(100, L3obi)


Jamal = IntrestRewardsAcct(1000, "Jamal")

Jamal.getBalance()

Jamal.deposit(100)



Jamal.transfer(100, Soultane)



Zineb = SavingsAcct(1000, "Zineb")
Zineb.getBalance()

Zineb.deposit(100)
Zineb.transfer(100, L3obi)

