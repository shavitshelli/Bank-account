from typing import Tuple
from bank.models.account import Account

class TransferService:
    """
    Service to handle money transfers between accounts.
    
    TODO List:
    1. Add timestamp to transfer records
    2. Implement transfer limits
    3. Add transaction fees
    4. Create transfer history method
    5. Add fraud detection
    6. Implement audit trails
    7. Add transfer cancellation
    8. Add transfer scheduling
    9. Implement transfer notifications
    10. Add transfer validation rules
    """
    def __init__(self):
        self.transfers = []

    def transfer(self, from_account: Account, to_account: Account, amount: float) -> Tuple[bool, str]:
        """
        Transfer money between two accounts.
        Returns (success: bool, message: str)
        """
        try:
            # Validate accounts are active
            if from_account.status != "ACTIVE" or to_account.status != "ACTIVE":
                return False, "One or both accounts are not active"

            # Validate sufficient balance
            if from_account.balance < amount:
                return False, "Insufficient funds"

            # Perform transfer
            from_account.withdraw(amount)
            to_account.deposit(amount)

            # Log transfer
            transfer_record = {
                "from_account": from_account.account_name,
                "to_account": to_account.account_name,
                "amount": amount,
                "timestamp": "TODO: Add timestamp"
            }
            self.transfers.append(transfer_record)

            return True, "Transfer successful"

        except ValueError as e:
            return False, str(e)
        except Exception as e:
            return False, f"Transfer failed: {str(e)}" 