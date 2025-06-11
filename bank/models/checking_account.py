# this class represents a checking account that a user has , it can direct to the user by owner_id
# it has an overdraft limit , and a balance

from account import Account,AccountType

class CheckingAccount(Account):
    OVERDRAFT_LIMIT = 1000
    def __init__(self, account_name, owner_id, initial_balance=0.0):
        super().__init__(account_name, owner_id, initial_balance)
        self.account_type = AccountType.CHECKING

    def withdraw(self, amount):
        try:
            super().withdraw(amount)
        except ValueError as e:
            raise e
        if self.balance - amount < -self.OVERDRAFT_LIMIT:
            raise ValueError(f"Can't withdraw more than the overdraft limit of {self.OVERDRAFT_LIMIT}")
        self.balance -= amount
        self.transactions.append(f"withdraw:{amount}")

    def get_account_type(self):
        return AccountType.CHECKING
