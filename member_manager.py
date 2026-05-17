class Member:
    def __init__(self, member_id, id, password, name, address):
        self.member_id = member_id
        self.id = id
        self.password = password
        self.name = name
        self.address = address

    def __str__(self):
        return f"회원번호: {self.member_id}, 아이디: {self.id}, 이름: {self.name}, 주소: {self.address}"


class MemberService:
    def __init__(self):
        self.member_list = []
        
    def create_member(self, id, password, name, address):
        member_id = len(self.member_list) + 1
        member = Member(member_id, id, password, name, address)
        self.member_list.append(member)
        return True

    def list_member(self):
        return self.member_list

    def update_member(self, user_id, password, name, address):
        for member in self.member_list:
            if member.id == user_id:
                member.password = password
                member.name = name
                member.address = address
                return True
        return False
        
    def delete_member(self, user_id):
        for member in self.member_list:
            if member.id == user_id:
                self.member_list.remove(member)
                return True
        return False


def select_menu():
    print('========================================================================')
    print('1. 회원가입 | 2. 회원목록 | 3. 회원상세정보 | 4. 회원정보수정 | 5. 회원탈퇴 | 0. 종료')
    print('========================================================================')
    menu = int(input('>> 메뉴 선택 :'))
    return menu


aservice = MemberService()

print()
print('==============회원관리============')

while True:
    # --- 추가된 부분: 입력 예외 처리 ---
    try:
        menu = select_menu()
    except ValueError:
        print('\n[오류] 문자가 입력되었습니다. 숫자로만 입력해주세요.\n')
        continue
    # -----------------------------------

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
            
    # 예외처리: 없는 메뉴 번호 입력 시 처리
    else:
        print('\n[오류] 0에서 5 사이의 올바른 메뉴 번호를 선택해주세요.\n')
    # ------------------------------------------------

print('\n프로그램을 종료합니다.')