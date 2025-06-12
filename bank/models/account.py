import time
from enum import Enum
from transaction_factory import TransactionFactory

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
        self.__status = Status.ACTIVE
        self.__transactions = []
        self.account_type = None
        self.__creation_date = time.time()
    
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("deposit must be positive")
        if self.status != Status.ACTIVE:
            raise ValueError("can't deposit to a disabled account")
        self.balance += amount
        self.transactions.append(TransactionFactory.create_deposit(amount, self.account_name))
    
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("withdraw must be positive")
        if self.status != Status.ACTIVE:
            raise ValueError("can't withdraw from a disabled account")
    
    def diactivate(self):
        if self.status == Status.DISABLED:
            raise ValueError("account is already disabled")
        self.status = Status.DISABLED
    
    def activate(self):
        if self.status == Status.ACTIVE:
            raise ValueError("account is already active")
        self.status = Status.ACTIVE
    
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
    def transactions(self):
        return self.__transactions

