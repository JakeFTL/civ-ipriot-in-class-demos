# Protecting/Hiding

# BankAccount
# - Create
# - Credit
# - Debit
# ACCESS MODIFIERS

class BankAccount:
    def __init__(self, account_number):
        self._account_number = account_number
        self._balance = 0
        self._passkey = 42

    def update_balance(self, amount):
        if self._balance - amount < 0:
            return "Insufficient Funds"
        self._balance -= amount

    def debit(self, amount):
        if amount < 0:
            raise ValueError("Amount must be positive")
        if self._balance
        self._balance -= amount

    def credit(self, amount):
        self._balance += amount

    def _update_database(self):
        ...

# abstraction
class Bird:
    def __init__(self):
        self._coordinate = 0, 0
        self._velocity = 0, 0

    def fly(self, direction):
        ...

    def flap_wings(self, frequency, intensity, pitch):
        ...

if __name__ == "__main__":
    jake = BankAccount(12345)
    jake.credit(100)
    jake.debit(20)

