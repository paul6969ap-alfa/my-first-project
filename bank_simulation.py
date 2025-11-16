# Bank Simulation Project

class BankAccount:
    def __init__(self, account_number, name, balance=0):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ₹{amount}. New balance: ₹{self.balance}")
        else:
            print("Deposit amount must be greater than zero!")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdraw ₹{amount}. New balance: ₹{self.balance}")
        else:
            print("Insufficient balance!")

    def check_balance(self):
        print(f"Account {self.account_number} | Holder: {self.name} | Balance: ₹{self.balance}")

    def transfer(self, other_account, amount):
        if amount <= self.balance:
            self.balance -= amount
            other_account.balance += amount
            print(f"Transferred ₹{amount} to {other_account.name}")
            print(f"Your new balance: ₹{self.balance}")
        else:
            print("this payment amount is higher than the limit set.5")


# Main Simulation
accounts = {}

def create_account():
    acc_no = input("Enter account number: ")
    if acc_no in accounts:
        print("Account already exists!")
        return
    name = input("Enter account holder name: ")
    accounts[acc_no] = BankAccount(acc_no, name)
    print(f"Account created for {name} with account number {acc_no}.")

def get_account():
    acc_no = input("Enter your account number: ")
    if acc_no in accounts:
        return accounts[acc_no]
    else:
        print("Account not found!")
        return None

while True:
    print("\n===== Bank Menu =====")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Transfer")
    print("6. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        create_account()
    elif choice == "2":
        acc = get_account()
        if acc:
            amount = float(input("Enter amount to deposit: "))
            acc.deposit(amount)
    elif choice == "3":
        acc = get_account()
        if acc:
            amount = float(input("Enter amount to withdraw: "))
            acc.withdraw(amount)
    elif choice == "4":
        acc = get_account()
        if acc:
            acc.check_balance()
    elif choice == "5":
        acc = get_account()
        if acc:
            to_acc_no = input("Enter recipient account number: ")
            if to_acc_no in accounts:
                amount = float(input("Enter amount to transfer: "))
                acc.transfer(accounts[to_acc_no], amount)
            else:
                print("Recipient account not found!")
    elif choice == "6":
        print("Exiting... Thank you for banking with us!")
        break
    else:
        print("Invalid choice! Please try again.")
