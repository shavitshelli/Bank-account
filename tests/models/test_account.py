import pytest
from bank.models import Account, Status

def test_account_creation():
    # Arrange
    account_name = "test_account"
    owner_id = "user123"
    initial_balance = 100.0

    # Act
    account = Account(account_name, owner_id, initial_balance)

    # Assert
    assert account.account_name == account_name
    assert account.owner == owner_id
    assert account.balance == initial_balance
    assert account.status == Status.ACTIVE
    assert len(account.transactions) == 0

def test_deposit_valid():
    # Arrange
    account = Account("test", "user123", 100.0)
    deposit_amount = 50.0

    # Act
    account.deposit(deposit_amount)

    # Assert
    assert account.balance == 150.0
    assert len(account.transactions) == 1
    assert "deposit:50.0" in account.transactions

def test_deposit_negative():
    # Arrange
    account = Account("test", "user123", 100.0)

    # Act & Assert
    with pytest.raises(ValueError, match="deposit must be positive"):
        account.deposit(-50.0)

def test_withdraw_valid():
    # Arrange
    account = Account("test", "user123", 100.0)
    withdraw_amount = 50.0

    # Act
    account.withdraw(withdraw_amount)

    # Assert
    assert account.balance == 50.0
    assert len(account.transactions) == 1
    assert "withdraw:50.0" in account.transactions

def test_withdraw_insufficient_funds():
    # Arrange
    account = Account("test", "user123", 100.0)

    # Act & Assert
    with pytest.raises(ValueError, match="insufficient balance"):
        account.withdraw(150.0)

def test_account_deactivation():
    # Arrange
    account = Account("test", "user123", 100.0)

    # Act
    account.diactivate()

    # Assert
    assert account.status == Status.DISABLED

def test_account_activation():
    # Arrange
    account = Account("test", "user123", 100.0)
    account.diactivate()

    # Act
    account.activate()

    # Assert
    assert account.status == Status.ACTIVE

def test_deposit_disabled_account():
    # Arrange
    account = Account("test", "user123", 100.0)
    account.diactivate()

    # Act & Assert
    with pytest.raises(ValueError, match="can't deposit to a disabled account"):
        account.deposit(50.0)

def test_withdraw_disabled_account():
    # Arrange
    account = Account("test", "user123", 100.0)
    account.diactivate()

    # Act & Assert
    with pytest.raises(ValueError, match="can't withdraw from a disabled account"):
        account.withdraw(50.0)