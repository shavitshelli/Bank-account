from user import User

class Bank:
    def __init__(self,bank_name,location,contact_info):
        self.bank_name = bank_name
        self.location = location
        self.contact_info = contact_info
        self.__users = {}
        self.__transactions = []

    def create_user(self, user_name, password, email):
        user = User(user_name, password, email)
        self.__users[user.user_id] = user
        return user
    
    def get_user(self, user_id):
        if user_id not in self.__users:
            raise ValueError(f"User {user_id} does not exist")
        return self.__users[user_id]
    
    def get_transaction(self, transaction_id):
        if transaction_id not in self.__transactions:
            raise ValueError(f"Transaction {transaction_id} does not exist")
        return self.__transactions[transaction_id]
    