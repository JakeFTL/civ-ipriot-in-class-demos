class Cat(object):
    ...



class BankAccount:
    def __init__(self, account_number):
        self.account_number = account_number
        self.balance = 0
        self.display_welcome_message()

    def close_account(self):
        print("Goodbye")
        del self

    def display_welcome_message(self):
        print("Welcome to HONEST bank!")


class SavingsAccount(BankAccount):
    def accrue_interest(self):
        self.balance *= 1.00000001


class CreditAccount(BankAccount):
    def __init__(self, account_number):
        super().__init__(account_number)
        self.credit_limit = 1000

    def charge_interest(self):
        super().display_welcome_message()
        self.balance *= 10000


account = BankAccount(56789)
savings = SavingsAccount(12345)
credit = CreditAccount(54321)
