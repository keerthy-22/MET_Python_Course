import threading
import time

class BankAccount:

    def __init__(self):
        self.balance = 5000
        self.transaction = []
        self.condition = threading.Condition()

    # Deposit Method
    def deposit(self, amount):
        with self.condition:
            self.balance += amount
            print(f"\nDeposited: {amount}")
            time.sleep(2)

            self.transaction.append(f"Deposited: {amount}")
            print("Deposit Successful.")
            print(f"Available Balance: {self.balance}")

            # Notify waiting threads
            self.condition.notify_all()

    # Withdraw Method
    def withdraw(self, amount):
        with self.condition:

            while self.balance < amount:
                print("\nInsufficient Balance.")
                print(f"Need {amount}, Available Balance: {self.balance}")
                print("Waiting for deposit...\n")
                self.condition.wait()

            print(f"\nWithdrawing: {amount}")
            time.sleep(2)

            self.balance -= amount
            self.transaction.append(f"Withdrawn: {amount}")

            print("Withdrawal Successful.")
            print(f"Available Balance: {self.balance}")

    # Check Balance
    def check_balance(self):
        with self.condition:
            print(f"\nCurrent Balance: {self.balance}")

    # Mini Statement
    def mini_statement(self):
        with self.condition:
            print("\n========== MINI STATEMENT ==========")

            if len(self.transaction) == 0:
                print("No Transactions Yet.")
            else:
                for t in self.transaction:
                    print(t)

            print("------------------------------------")
            print(f"Current Balance: {self.balance}")
            print("====================================")


# Create Object
account = BankAccount()

# Create Threads
t1 = threading.Thread(target=account.withdraw, args=(10000,))
t2 = threading.Thread(target=account.deposit, args=(7000,))
t3 = threading.Thread(target=account.mini_statement)

# Start Threads
t1.start()
t2.start()

# Wait until withdraw and deposit finish
t1.join()
t2.join()

# Print mini statement at the end
t3.start()
t3.join()
