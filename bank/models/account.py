import time
from enum import Enum

class Status(Enum):
    ACTIVE = "active"
    DISABLED = "disabled"

class AccountType(Enum):
    CHECKING = "checking"
    SAVINGS = "savings"

#This class represents an account that a user has , it can direct to the user by owner_id
#It has a balance and a status , it can be active or disabled
#It can be a checking or savings account
#It can have a name and a creation date
#It can have transactions
#It can be activated or disabled
#It can be summarized
#It can be deposited or withdrawn from


class Account:
    def __init__(self, account_name, owner_id, initial_balance=0.0):
        self.account_name = account_name
        self.owner = owner_id
        self.balance = initial_balance
        self.status = "ACTIVE"
        self.transactions = []
        self.account_type = None
        self.__creation_date = time.time()
    
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("deposit must be positive")
        if self.status != "ACTIVE":
            raise ValueError("can't deposit to a disabled account")
        self.balance += amount
        self.transactions.append(f"deposit:{amount}")
    
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("withdraw must be positive")
        if self.status != "ACTIVE":
            raise ValueError("can't withdraw from a disabled account")
        if self.balance < amount:
            raise ValueError("insufficient balance")
        self.balance -= amount
        self.transactions.append(f"withdraw:{amount}")
    
    def diactivate(self):
        self.status = "DISABLED"
    
    def activate(self):
        self.status = "ACTIVE"
    
    def get_account_type(self):
        raise NotImplementedError("subclass must implement this method")
    
    def account_summary(self):
        return f"Account Name: {self.account_name}\nOwner: {self.owner}\nBalance: {self.balance}\nStatus: {self.status}\nTransactions: {self.transactions}"

    @property
    def creation_date(self):
        return self.__creation_date
    
    @property
    def status(self):
        return self.status
    
    @property
    def owner(self):
        return self.owner
    
    @property
    def account_name(self):
        return self.account_name
    
    @property
    def transactions(self):
        return self.transactions
    

class CheckingAccount(Account):
    def __init__(self, account_name, owner_id, initial_balance=0.0):
        super().__init__(account_name, owner_id, initial_balance)
        self.account_type = AccountType.CHECKING
        self.overdraft_limit = 1000.0  # Example overdraft limit

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("withdraw must be positive")
        if self.status != "ACTIVE":
            raise ValueError("can't withdraw from a disabled account")
        if self.balance + self.overdraft_limit < amount:
            raise ValueError("insufficient balance and overdraft limit")
        self.balance -= amount
        self.transactions.append(f"withdraw:{amount}")

class SavingsAccount(Account):
    def __init__(self, account_name, owner_id, initial_balance=0.0):
        super().__init__(account_name, owner_id, initial_balance)
        self.account_type = AccountType.SAVINGS
        self.interest_rate = 0.02  # 2% interest rate
        self.minimum_balance = 100.0

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("withdraw must be positive")
        if self.status != "ACTIVE":
            raise ValueError("can't withdraw from a disabled account")
        if self.balance - amount < self.minimum_balance:
            raise ValueError(f"withdrawal would bring balance below minimum required {self.minimum_balance}")
        if self.balance < amount:
            raise ValueError("insufficient balance")
        self.balance -= amount
        self.transactions.append(f"withdraw:{amount}")

    def add_interest(self):
        if self.status == "ACTIVE":
            interest = self.balance * self.interest_rate
            self.balance += interest
            self.transactions.append(f"interest:{interest}")

