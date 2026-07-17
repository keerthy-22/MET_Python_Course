class BankAccount:
    def __init__(self, holder_name, account_number, balance):
        self.holder_name = holder_name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("₹", amount, "deposited successfully.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("₹", amount, "withdrawn successfully.")
        else:
            print("Insufficient balance. Withdrawal failed.")

    def display_balance(self):
        print("\nAccount Details")
        print("Account Holder:", self.holder_name)
        print("Account Number:", self.account_number)
        print("Current Balance: ₹", self.balance)


# Create an object
account1 = BankAccount("Bhuvana", 1234567890, 10000)

# Display balance
account1.display_balance()

# Deposit money
account1.deposit(2000)

# Withdraw money
account1.withdraw(5000)

# Try to withdraw more than available balance
account1.withdraw(10000)

# Display final balance
account1.display_balance()
