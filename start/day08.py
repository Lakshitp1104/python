class Account:
    def  __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc

    def debit(self, amount):
        self.balance -= amount
        print("RS",amount, "debited")
        print("total balance:", self.get_balance())

    def credit(self, amount):
        self.balance += amount
        print("RS",amount, "credited")
        print("total balance:", self.get_balance())

    def get_balance(self):
        return self.balance
    
a1 = Account(1000, 12345)
a1.debit(500)
a1.credit(200)
a1.debit(300)