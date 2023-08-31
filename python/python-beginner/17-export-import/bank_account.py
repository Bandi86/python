class BankAccount:
    def __init__(self, owner, balance, action):
        self.owner = owner
        self.balance = balance
        self.action = action
    
    def account_details(self):
        print(f"A tulajdonos: {self.owner} Az egyenleg: {self.balance}")    