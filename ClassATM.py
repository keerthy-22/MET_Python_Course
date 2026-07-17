class ATMAccount:
    def __init__(self, account_holder, pin, balance):
        self.account_holder = account_holder
        self.pin = pin
        self.balance = balance

    def check_balance(self):
        print("Current Balance: ₹", self.balance)

    def deposit(self, amount):
        self.balance += amount
        print("₹", amount, "deposited successfully.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("₹", amount, "withdrawn successfully.")
        else:
            print("Insufficient Balance!")

    def change_pin(self, old_pin, new_pin):
        if old_pin == self.pin:
            self.pin = new_pin
            print("PIN changed successfully.")
        else:
            print("Incorrect old PIN.")

    def display_details(self):
        print("\n------ ATM Account Details ------")
        print("Account Holder :", self.account_holder)
        print("Balance        : ₹", self.balance)


# User Input
account_holder = input("Enter Account Holder Name: ")
pin = int(input("Set a 4-digit PIN: "))
balance = float(input("Enter Initial Balance: "))

# Create Object
account = ATMAccount(account_holder, pin, balance)

# Display Details
account.display_details()

# Deposit Money
amount = float(input("\nEnter Amount to Deposit: "))
account.deposit(amount)

# Withdraw Money
amount = float(input("Enter Amount to Withdraw: "))
account.withdraw(amount)

# Check Balance
account.check_balance()

# Change PIN
old_pin = int(input("\nEnter Old PIN: "))
new_pin = int(input("Enter New PIN: "))
account.change_pin(old_pin, new_pin)

# Final Details
account.display_details()
