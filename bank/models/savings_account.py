#this class represents a savings account that a user has , it can direct to the user by owner_id
# it has interest rate , minimum balance , withdraw limit per period , withdraw count , and a balance
# it can withdraw , deposit , add interest , reset withdraw count , and get the minimum balance


from account import Account,AccountType
from transaction_factory import TransactionFactory
class SavingsAccount(Account):
    def __init__(self, account_name, owner_id, initial_balance=0.0):
        super().__init__(account_name, owner_id, initial_balance)
        self.account_type = AccountType.SAVINGS
        self.interest_rate = 0.02
        self.minimum_balance = 1000
        self.withdraw_limit_per_period = 3
        self.withdraw_count = 0

    
    def withdraw(self, amount):
        try:
            super().withdraw(amount)
        except ValueError as e:
            raise e
        if self.balance - amount < 0:
            raise ValueError("Can't withdraw more than the balance")
        if self.withdraw_count >= self.withdraw_limit_per_period:
            raise ValueError("Can't withdraw more than the limit per period")
        self.balance -= amount
        self.transactions.append(TransactionFactory.create_withdraw(amount, self.account_name))
        self.withdraw_count += 1

    def get_account_type(self):
        return AccountType.SAVINGS
    
    def get_interest_rate(self):
        return self.interest_rate
    
    def add_interest(self):
        if self.balance < self.minimum_balance:
            raise ValueError("Can't add interest to an account with less than the minimum balance")
        self.balance += self.balance * self.interest_rate
        self.transactions.append(f"add_interest:{self.balance * self.interest_rate}")

    def reset_withdraw_count(self):
        self.withdraw_count = 0

    def minimum_balance(self):
        return self.minimum_balance