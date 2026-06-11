class Account():

    def __init__(self, account_no, owner, balance, password ):
        self.__account_no = account_no
        self.__owner = owner
        self.__balance = balance
        self.__password = password

    def get_account_no(self):
        return self.__account_no
    def get_owner(self):
        return self.__owner
    def get_balance(self):
        return self.__balance
    def get_pasword(self):
        return self.__password
    
    def set_account_no(self, account_no):
        self.__account_no = account_no

    def set_balance(self, balance):
        self.__balance = balance

    def __str__(self):
        return f'전화번호 = {self.__account_no}, 사용자 = {self.__owner}, 잔액 = {self.__balance}, 비밀번호 = {self.__password}'
    
if __name__ == '__main__':
    ac = Account('01045088860', '이유찬', 1000, '4023')
    ac.set_balance
    print(ac)
    print(ac.get_account_no())
