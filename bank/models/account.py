import time
from enum import Enum
class Status(Enum):
    ACTIVE = "active"
    DISABLED = "disabled"
#This class represents an account that a user has , it can direct to the user by owner_id
#It has a balance and a status , it can be active or disabled
#It can be a checking or savings account
#It can have a name and a creation date
#It can have transactions
#It can be activated or disabled
#It can be summarized
#It can be deposited or withdrawn from


class Account:
    def __init__(self,account_name,owner_id,balance):
        self._account_name = account_name
        self.__owner = owner_id 
        self.__balance = balance
        self.__creation_date = time.time()
        self.__transactions = []
        self.__status = Status.ACTIVE
    
    def deposit(self,amount):
        if self.__status == Status.DISABLED:
            raise ValueError("can't deposit to a disabled account")
        if amount < 0:
            raise ValueError("deposit must be positive")
        self.__balance += amount
        self.__transactions.append(f"deposit:{amount}")
    
    def withdraw(self,amount):
        if self.__status == Status.DISABLED:
            raise ValueError("can't withdraw from a disabled account")
        if amount < 0:
            raise ValueError("withdrawal must be positive")
        if amount >self.__balance:
            raise ValueError("insufficient balance")
        self.__balance-=amount
        self.__transactions.append(f"withdraw:{amount}")
    
    def diactivate(self):
        if self.__status == Status.ACTIVE:
            self.__status = Status.DISABLED
        else:
            raise ValueError("can't disable an already disabled account")
    
    def activate(self):
        if self.__status == Status.DISABLED:
            self.__status = Status.ACTIVE
        else:
            raise ValueError("can't activate an already active account")
    
    def get_account_type(self):
        raise NotImplementedError("subclass must implement this method")
    
    def account_summary(self):
        return f"Account Name: {self._account_name}\nOwner: {self.__owner}\nBalance: {self.__balance}\nStatus: {self.__status}\nTransactions: {self.__transactions}"

    @property
    def balance(self):
        return self.__balance
    
    @property
    def status(self):
        return self.__status
    
    @property
    def owner(self):
        return self.__owner
    
    @property
    def account_name(self):
        return self._account_name
    
    @property
    def transactions(self):
        return self.__transactions
    

