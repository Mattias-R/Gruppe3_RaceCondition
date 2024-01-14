import threading

class BankAccount:
    def __init__(self, balance):
        self.balance = balance
        self.lock = threading.Lock()

    def deposit(self, amount):
        with self.lock:
            new_balance = self.balance + amount
            self.balance = new_balance
            print("new Balance after Deposit: " + str(new_balance))

    def withdraw(self, amount):
        with self.lock:
            if self.balance >= amount:
                new_balance = self.balance - amount
                self.balance = new_balance
                print("new Balance after Withdraw: " + str(new_balance))

def deposit_function(account, amount, times):
    for _ in range(times):
        account.deposit(amount)

def withdraw_function(account, amount, times):
    for _ in range(times):
        account.withdraw(amount)

# Example Usage
initial_balance = 5000
account = BankAccount(initial_balance)

# Creating threads
deposit_thread = threading.Thread(target=deposit_function, args=(account, 5, 1000))
withdraw_thread = threading.Thread(target=withdraw_function, args=(account, 5, 1000))

# Starting threads
deposit_thread.start()
withdraw_thread.start()

# Joining threads
deposit_thread.join()
withdraw_thread.join()

print(f"Final Balance: {account.balance}")
