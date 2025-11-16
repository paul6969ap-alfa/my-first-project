class bankaccount():
    def __init__(self,acc_no,name,balance=0):
        self.acc_no = acc_no
        self.name = name
        self.balance = balance

    
    def deposit(self,amount):
        if amount > 0:
            self.balance += amount 
            print(f"your account no {self.acc_no} is credited with {self.balance}")
  
        else:
            print(f"enter a valid amount")

    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"your acc no {self.acc_no} is debited with ₹{amount}. your new balance is {self.balance}" )
        else:
            print(f"not enough balance.")  

    def check_balance(self):
        print(f"Account {self.acc_no} | Holder: {self.name} | Balance: ₹{self.balance}")       

    
    def transfer(self,other_acc,amount):
        if amount <= self.balance:
            self.balance -= amount
            other_acc.balance += amount
            print(f"₹{amount} is transfered to {other_acc.name}")
            print(f"your new bank balance is {self.balance}")
        else:
            print(f"this payment amount is higher than your balance amount,\nyour balance is {self.balance}.")    

   

    # def withdraw(self, amount):
    #     if amount <= self.balance:
    #         self.balance -= amount
    #         print(f"Withdraw ₹{amount}. New balance: ₹{self.balance}")
    #     else:
    #         print("Insufficient balance!")

    # def check_balance(self):
    #     print(f"Account {self.acc_no} | Holder: {self.name} | Balance: ₹{self.balance}")

    # def transfer(self, other_account, amount):
    #     if amount <= self.balance:
    #         self.balance -= amount
    #         other_account.balance += amount
    #         print(f"Transferred ₹{amount} to {other_account.name}")
    #         print(f"Your new balance: ₹{self.balance}")
    #     else:
    #         print("this payment amount is higher than the limit set.5")


# Main Simulation
accounts = {}



def create_account():
    acc_no = input("Enter account number: ")
    if acc_no in accounts:
        print("Account already exists!")
        return
    name = input("Enter account holder name: ")
    accounts[acc_no] = bankaccount(acc_no, name)
    print(f"hi Mr.{name},welcome to AMIT STANDARD BANK.")
    print(f"Account created for {name} with account number {acc_no}.")

def get_account():
    acc_no = input("Enter your account number: ")
    if acc_no in accounts:
        return accounts[acc_no]
    else:
        print("Account not found!")
        return None

while True:
    print("\n AMIT STANDARD BANK")
    print("\n===== Bank Menu =====")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Transfer")
    print("6. Exit")
    choice = input("Enter your choice: ")

    # if choice == "1":
    #     create_account()
    # elif choice == "2":
    #     acc_n = get_account()
    #     if acc_n :
    #         amount = float(input("Enter amount to deposit: "))
    #         acc_n.deposit(amount)

    # elif choice == "3":
    #     acc_n = get_account()
    #     if acc_n :
    #         amount = float(input("Enter amount to withdraw: "))
    #         acc_n.withdraw(amount)

    # elif choice == "4":
    #     acc_no = get_account()
    #     if acc_n :
    #         acc_n.check_balance()

    # elif choice == "5":
    #     acc_n = get_account()
    #     if acc_n :
    #         to_acc_no = input("please, enter recipent account number: ")
    #         if to_acc_no in accounts:
    #             amount = float(input("please, enter amount to transfer:"))
    #             acc_n.transfer(accounts[to_acc_no], amount)
    #         else:
    #             print("sorry, Recipient account not found!")

    # elif choice == "6":
    #     print("Exiting... Thank you for banking with us!")
    #     break
    # else:
    #     print("Invalid choice! Please try again.")
           



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


print("this is change for my second commit")