from .account import Account

class AccountDAO:
    def __init__(self):
        self.__accountDB = {}

    def insert_account(self, account):
        if self.is_exist(account.get_account_no()):
            return False
        self.__accountDB[account.get_account_no()] = account
        return True

    def is_exist(self, account_no):
        return account_no in self.__accountDB

    def get_account_info(self, account_no):
        if self.is_exist(account_no):
            return self.__accountDB[account_no]
        return None

    def get_all_accounts(self):
        return list(self.__accountDB.values())

    def update_account(self, account_no, account):
        if self.is_exist(account_no):
            self.__accountDB[account_no] = account
            return True
        return False

    def remove_account(self, account_no):
        if self.is_exist(account_no):
            self.__accountDB.pop(account_no)
            return True
        return False


if __name__ == '__main__':
    dao = AccountDAO()
    ac = Account('01045088860', '이유찬', 1000, '4023')
    dao.insert_account(ac)
    print(dao.get_account_info('01045088860'))
    print(dao.get_all_accounts())
