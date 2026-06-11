from .account import Account
from .account_dao import AccountDAO

class AccountService:
    def __init__(self, account_dao):
        self.dao = account_dao

    def create_account(self, account_no, owner, balance, password):
        if self.dao.is_exist(account_no):
            return False
        account = Account(account_no, owner, balance, password)
        self.dao.insert_account(account)
        return True

    def deposit(self, account_no, amount):
        account = self.dao.get_account_info(account_no)
        if not account:
            return False
        account.set_balance(account.get_balance() + amount)
        return True

    def withdraw(self, account_no, password, amount):
        account = self.dao.get_account_info(account_no)
        if not account:
            return False
        if account.get_pasword() != password:
            return False
        if account.get_balance() < amount:
            return False
        account.set_balance(account.get_balance() - amount)
        return True

    def transfer(self, from_no, password, to_no, amount):
        if self.withdraw(from_no, password, amount):
            return self.deposit(to_no, amount)
        return False

    def get_balance(self, account_no):
        account = self.dao.get_account_info(account_no)
        if account:
            return account.get_balance()
        return None

    def get_account_info(self, account_no):
        return self.dao.get_account_info(account_no)

    def get_all_accounts(self):
        return self.dao.get_all_accounts()

    def remove_account(self, account_no):
        return self.dao.remove_account(account_no)


if __name__ == '__main__':
    svc = AccountService(AccountDAO())
    svc.create_account('01045088860', '이유찬', 1000, '4023')
    svc.create_account('01012345678', '홍길동', 5000, '1234')
    print(svc.get_account_info('01045088860'))
    svc.deposit('01045088860', 500)
    print(svc.get_balance('01045088860'))
    svc.withdraw('01045088860', '4023', 200)
    print(svc.get_balance('01045088860'))
    svc.transfer('01012345678', '1234', '01045088860', 1000)
    print(svc.get_balance('01045088860'))
    print(svc.get_balance('01012345678'))
