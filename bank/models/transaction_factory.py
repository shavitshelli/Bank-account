from transaction import Transaction, TransactionType

class TransactionFactory:
    @staticmethod
    def create_deposit(amount, account_name):
        return Transaction(amount, TransactionType.DEPOSIT, account_name)
    
    @staticmethod
    def create_withdraw(amount, account_name):
        return Transaction(amount, TransactionType.WITHDRAW, account_name)
    
    @staticmethod
    def create_transfer_out(amount, account_name):
        return Transaction(amount, TransactionType.TRANSFER_OUT, account_name)
    
    @staticmethod
    def create_transfer_in(amount, account_name):
        return Transaction(amount, TransactionType.TRANSFER_IN, account_name)
    
