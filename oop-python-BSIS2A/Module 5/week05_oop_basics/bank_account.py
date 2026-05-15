# Name: Bostero, Alexa C.

class BankAccount_acb:
    def __init__(self, account_name_acb, balance_acb):
        self.account_name_acb = account_name_acb
        self.balance_acb = balance_acb

    def deposit_acb(self, amount_acb):
        self.balance_acb += amount_acb
        print("Deposit successful")

    def withdraw_acb(self, amount_acb):
        if amount_acb <= self.balance_acb:
            self.balance_acb -= amount_acb
            print("Withdrawal successful")
        else:
            print("Insufficient balance")

    def display_balance_acb(self):
        print("Balance:", self.balance_acb)


account_acb = BankAccount_acb("Juan", 5000)
account_acb.deposit_acb(1000)
account_acb.withdraw_acb(2000)
account_acb.display_balance_acb()