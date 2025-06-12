from datetime import datetime
from enum import Enum

class TransactionType(Enum):
    DEPOSIT = "deposit"
    WITHDRAW = "withdraw"
    TRANSFER_OUT = "transfer_out"
    TRANSFER_IN = "transfer_in"


class TransactionStatus(Enum):
    PENDING = "pending"
    COMPLETE = "complete"
    FAILE = " fail" 


class Transaction:
    ID=1
    def __init__(self, amount, transaction_type, account_name):
        self.id = Transaction.ID
        Transaction.ID += 1
        self._amount = amount
        self.transaction_type = transaction_type
        self.account_name = account_name
        self.__date = datetime.now()
        self.__status = TransactionStatus.PENDING
    
    def get_transaction_type(self):
        return self.transaction_type
    
    @property
    def amount(self):
        return self._amount
    
    def get_account_name(self):
        return self.account_name
    
    @property
    def date(self):
        return self.__date
    
    def get_id(self):
        return self.id
    
    @property
    def status(self):
        return self.__status
    
    @status.setter
    def status(self, status):
        self.__status = status

   
    

    