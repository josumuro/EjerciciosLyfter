class BankAccount:
    def __init__(self):
        self.balance = 0

    def add_balance(self, amount):
        self.balance += amount
        print(f"Balance added: {amount}. Current balance: {self.balance}")

    def withdraw_balance(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Balance withdrawn: {amount}. Current balance: {self.balance}")
        else:
            print("Insufficient balance.")

class SavingsAccount(BankAccount):
    def __init__(self,minimum_balance):
        super().__init__()
        self.minimum_balance = minimum_balance
        if self.balance < self.minimum_balance:
            print(f"Initial balance is less than the minimum balance of {self.minimum_balance}. Please add funds to meet the minimum balance requirement.")

  
# Example usage:
savings_account = SavingsAccount(minimum_balance=100)   
savings_account.add_balance(50)  
savings_account.add_balance(60)  
savings_account.withdraw_balance(30)  
savings_account.withdraw_balance(80)   
        