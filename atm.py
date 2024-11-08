import time

# ATM Machine Simulation

class ATM:
    def __init__(self, pin):
        self.balance = 0.0  # Initial balance set to zero
        self.pin = pin  # Default PIN
        self.transaction_history = []  # To store transaction history
    
    def check_pin(self, input_pin):
        """Checks if the entered PIN matches the user's PIN."""
        return self.pin == input_pin
    
    def account_balance(self):
        """Returns the current account balance."""
        print("\n--------------------------------")
        print(f"Your current balance is: ₹{self.balance}")
        print("--------------------------------")
        self.transaction_history.append(f"Checked balance: ₹{self.balance}")
        time.sleep(1)

    def deposit_cash(self, amount):
        """Deposits the specified amount into the account."""
        if amount > 0:
            self.balance += amount
            print("\n--------------------------------")
            print(f"₹{amount} has been deposited to your account.")
            print("--------------------------------")
            self.transaction_history.append(f"Deposited: ₹{amount}")
        else:
            print("\nDeposit amount must be positive.")
        time.sleep(1)

    def withdraw_cash(self, amount):
        """Withdraws the specified amount from the account if sufficient funds are available."""
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print("\n--------------------------------")
                print(f"₹{amount} has been withdrawn from your account.")
                print("--------------------------------")
                self.transaction_history.append(f"Withdrew: ₹{amount}")
            else:
                print("\nInsufficient balance.")
        else:
            print("\nWithdrawal amount must be positive.")
        time.sleep(1)
    
    def change_pin(self, old_pin, new_pin):
        """Changes the user's PIN if the old PIN is entered correctly."""
        if self.check_pin(old_pin):
            self.pin = new_pin
            print("\n--------------------------------")
            print("PIN changed successfully.")
            print("--------------------------------")
            self.transaction_history.append("Changed PIN")
        else:
            print("\nIncorrect old PIN.")
        time.sleep(1)
    
    def show_transaction_history(self):
        """Displays the transaction history."""
        print("\n--------------------------------")
        if self.transaction_history:
            print("Transaction History:")
            for transaction in self.transaction_history:
                print(transaction)
        else:
            print("No transactions yet.")
        print("--------------------------------")
        time.sleep(1)

# ATM Simulation Code
atm_pin = 1234  # Default PIN for simulation purposes
atm = ATM(atm_pin)

print("=================================")
print("   Welcome to the ATM Machine!   ")
print("=================================")
time.sleep(1)

input_pin = int(input("Please enter your PIN: "))
time.sleep(1)

# Verifying the entered PIN
if atm.check_pin(input_pin):
    print("\nPIN Verified! Access Granted.")
    time.sleep(1)
    while True:
        print("\n=================================")
        print("             ATM Menu            ")
        print("=================================")
        print("1. Balance Inquiry")
        print("2. Cash Deposit")
        print("3. Cash Withdrawal")
        print("4. Change PIN")
        print("5. Transaction History")
        print("6. Exit")
        print("=================================")

        choice = input("Choose an option (1-6): ")
        time.sleep(1)
        
        match choice:
            case "1":
                atm.account_balance()
            case "2":
                deposit_amount = float(input("Enter amount to deposit: ₹"))
                atm.deposit_cash(deposit_amount)
            case "3":
                withdrawal_amount = float(input("Enter amount to withdraw: ₹"))
                atm.withdraw_cash(withdrawal_amount)
            case "4":
                old_pin = int(input("Enter your current PIN: "))
                new_pin = int(input("Enter your new PIN: "))
                atm.change_pin(old_pin, new_pin)
            case "5":
                atm.show_transaction_history()
            case "6":
                print("\nThank you for using the ATM. Goodbye!")
                print("=================================")
                time.sleep(1)
                break
            case _:
                print("\nInvalid choice. Please try again.")
                time.sleep(1)
else:
    print("\nIncorrect PIN. Access denied.")
    print("=================================")
    time.sleep(1)
