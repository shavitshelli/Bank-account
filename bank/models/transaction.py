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
        self.date = datetime.now()
    
    def get_transaction_type(self):
        return self.transaction_type
    
    @property
    def amount(self):
        return self._amount
    
    def get_account_name(self):
        return self.account_name
    
    def get_date(self):
        return self.date
    
    def get_id(self):
        return self.id
    