# this class represents a user that has accounts
# it can create accounts , close accounts , deposit , withdraw , and get the balance
# it can list the accounts
# it can get the account details

from checking_account import CheckingAccount
from savings_account import SavingsAccount
from account import AccountType

class User:
    USER_ID = 0
    def __init__(self,user_name,password,email):
        self._user_name = user_name
        self.__password = password
        self.email = email
        self.__accounts = {}
        self.user_id = User.USER_ID
        User.USER_ID += 1
    
    def deposit(self,account_name,amount):
        if not self.__account_exists(account_name):
            raise ValueError(f"Account {account_name} does not exist")
        self.__accounts[account_name].deposit(amount)
    
    def withdraw(self,account_name,amount):
        if not self.__account_exists(account_name):
            raise ValueError(f"Account {account_name} does not exist")
        self.__accounts[account_name].withdraw(amount)
        
    def list_accounts(self):
        return list(self.__accounts.keys())

    def __account_exists(self,account_name):
        return account_name in self.__accounts
    
    def create_account(self,account_name,account_type,initial_deposit):
        if self.__account_exists(account_name):
            raise ValueError("This account already exists")
        if initial_deposit < 0:
            raise ValueError("Initial deposit must be positive")
        if account_type == AccountType.CHECKING:
            account = CheckingAccount(account_name, self.user_id, initial_deposit)
        elif account_type == AccountType.SAVINGS:
            account = SavingsAccount(account_name, self.user_id, initial_deposit)
        else:
            raise ValueError("Invalid account type")
        self.accounts.append(account)
        return account
    
    def close_account(self,account_name):
        if not self.__account_exists(account_name):
            raise ValueError("Account: {account_name} does not exist")
        try:
            self.__accounts[account_name].diactivate()
        except ValueError as e:
            raise ValueError(f"{e}")
        return f"Account: {account_name} closed successfully"
    
    def get_balance(self, account_name):
        if not self.__account_exists(account_name):
            raise ValueError(f"Account {account_name} does not exist")
        return self.__accounts[account_name].balance
    
    def get_account(self, account_name):
        if not self.__account_exists(account_name):
            raise ValueError(f"Account {account_name} does not exist")
        return self.__accounts[account_name]
    
    

