class Account:
    def __init__(self, account_no, owner, balance):
        self.account_no = account_no
        self.owner = owner
        self.balance = balance
        
    def __str__(self):
        return f'{self.account_no} \t{self.owner} \t{self.balance}'
        
    def deposit(self, amount):
        self.balance += amount
        
    def withdraw(self, amount):
        self.balance -= amount
        
    def get_account_no(self):
        return self.account_no
        
    def get_owner(self):
        return self.owner
        
    def get_balance(self):
        return self.balance


class AccountService:
    def __init__(self):
        self.account_list = []
        
    def create_account(self, account_no, owner, balance):
        account = Account(account_no, owner, balance)
        self.account_list.append(account)
        return True
        
    def list_account(self):
        return self.account_list
        
    def deposit(self, account_no, amount):
        for account in self.account_list:
            if account.get_account_no() == account_no:
                account.deposit(amount)
                break
                
    def withdraw(self, account_no, amount):
        for account in self.account_list:
            if account.get_account_no() == account_no:
                account.withdraw(amount)
                break
if __name__ == '__main__':
    aservice = AccountService()
    aservice.create_account('111-111', 'hye', 5500)
    alist = aservice.list_account()
    for account in alist:
        print(account)
    aservice.deposit('111-111', 10000)
    for account in aservice.list_account():
        print(account)