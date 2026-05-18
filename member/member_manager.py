from member import MemberService

ms = MemberService()

aservice = MemberService()

print()
print('==============회원관리============')

def select_menu():
    print('========================================================================')
    print('1. 회원가입 | 2. 회원목록 | 3. 회원상세정보 | 4. 회원정보수정 | 5. 회원탈퇴 | 0. 종료')
    print('========================================================================')
    menu = int(input('>> 메뉴 선택 :'))
    return menu

while True:
    menu = select_menu()

    if menu == 0:
        break
        
    elif menu == 1:
        user_id = input(">> 아이디 : ")
        password = input(">> 비밀번호 : ")
        name = input(">> 이름 : ")
        address = input(">> 주소 : ")
        
        if aservice.create_member(user_id, password, name, address):
            print('결과 : 회원이 등록되었습니다 ')
            
    elif menu == 2:
        member_list = aservice.list_member()
        print('회원목록')
        for member in member_list:
            print(f"회원번호: {member.member_id}, 이름: {member.name}")
            
    elif menu == 3:
        member_list = aservice.list_member()
        print('회원상세정보')
        for member in member_list:
            print(member)
            
    elif menu == 4:
        print('회원정보수정')
        user_id = input(">> 수정할 회원의 아이디 : ")
        password = input(">> 새 비밀번호 : ")
        name = input(">> 새 이름 : ")
        address = input(">> 새 주소 : ")
        
        if aservice.update_member(user_id, password, name, address):
            print('결과 : 회원정보가 성공적으로 수정되었습니다.')
        else:
            print('결과 : 해당 아이디를 가진 회원이 존재하지 않습니다.')
            
    elif menu == 5:
        print('회원탈퇴')
        user_id = input(">> 탈퇴할 회원의 아이디 : ")
        
        if aservice.delete_member(user_id):
            print('결과 : 회원탈퇴가 성공적으로 처리되었습니다.')
        else:
            print('결과 : 해당 아이디를 가진 회원이 존재하지 않습니다.')