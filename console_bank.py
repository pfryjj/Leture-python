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


def select_menu():
    print('========================================================')
    print('1. 계좌생성 | 2. 계좌 목록 | 3. 입금 | 4. 출금 | 0. 종료')
    print('========================================================')
    menu = int(input('>> 메뉴 선택 :'))
    return menu


aservice = AccountService()

print()
print('========================Hyejeong Bank==================')
while True:
    menu = select_menu()
    
    if menu == 0: 
        break
        
    elif menu == 1:
        account_no = input(">> 계좌번호 : ")
        owner = input(">> 계좌주 : ")
        balance = int(input(">> 초기입금액 : "))
        
        if aservice.create_account(account_no, owner, balance):
            print('결과 : 계좌가 생성되었습니다.')
            
    elif menu == 2:
        account_list = aservice.list_account()
        print('  계좌목록')
        for account in account_list:
            print(account)
            
    elif menu == 3:
        print('예금')
        account_no = input('> 계좌번호: ')
        amount = int(input('> 예금액 : '))
        aservice.deposit(account_no, amount)
        print('결과 : 입금이 완료되었습니다.')
        
    elif menu == 4:
        print('출금')
        account_no = input('> 계좌번호: ')
        amount = int(input('> 출금액 : '))
        aservice.withdraw(account_no, amount)
        print('결과 : 출금이 완료되었습니다.')
    elif menu == 5:

print('============ 이용해 주셔서 감사합니다.==============')