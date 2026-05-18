from account.account import AccountService

def select_menu():
    print('========================================================')
    print('1. 계좌생성 | 2. 계좌 목록 | 3. 입금 | 4. 출금 | 0. 종료')
    print('========================================================')
    menu = int(input('>> 메뉴 선택 :'))
    return menu


aservice = AccountService()
def start_console_bank(aservice):
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
        else:
            print('잘못된 메뉴입니다. 다시 선택해주세요.')

    print('============ 이용해 주셔서 감사합니다.==============')

if __name__ == '__main__':
    aservice = AccountService()
    start_console_bank(aservice)