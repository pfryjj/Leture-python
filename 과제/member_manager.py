from member import Member, MemberDAO, MemberService

class MemberManager:
    start_menu = ['종료', '로그인', '회원가입']
    admin_menu = ['로그아웃', '회원목록', '회원정보조회', '회원탈퇴']
    member_menu = ['로그아웃', '내정보조회', '내정보수정', '회원탈퇴']
    ADMIN_ID = 'admin'
    ADMIN_PASSWORD = '1234'

    def __init__(self):
        self.current_user = None
        self.ms = MemberService(MemberDAO())

    def main(self):
        self.show_welcome()
        self.ms.join(Member(MemberManager.ADMIN_ID, MemberManager.ADMIN_PASSWORD, None))
        while True:
            menu = self.select_menu(MemberManager.start_menu)
            if menu == 0: break
            elif menu == 1: # 로그인
                id = input('>> id : ')
                password = input('>> password : ')
                self.current_user = self.ms.login(id, password)
                if self.current_user:
                    if self.current_user == MemberManager.ADMIN_ID:
                        self.start_admin_menu()
                    else:
                        self.start_member_menu()
                else:
                    print('로그인 실패.')

            elif menu == 2: # 회원가입
                id = input('>> id : ')
                password = input('>> password : ')
                name = input('>> name : ')
                member = Member(id, password, name)
                if self.ms.join(member):
                    print('회원가입 완료.')
                else:
                    print('회원가입 실패.')
            else:
                print('없는 메뉴.')
        self.say_goodbye()

    def start_admin_menu(self):
        print('---------- 관리자 메뉴 ----------')
        while True:
            menu = self.select_menu(MemberManager.admin_menu)
            if menu == 0: # 로그아웃
                self.current_user = None
                print('로그아웃.')
                break
            elif menu == 1: # 회원목록
                self.list_all_member()
            elif menu == 2: # 회원정보조회
                id = input('>> 조회할 id : ')
                member = self.ms.view_member_info(id)
                if member:
                    print(member)
                else:
                    print('존재하지 않는 회원.')
            elif menu == 3: # 회원강퇴(회원탈퇴)
                id = input('>> 강퇴할 id : ')
                if id == MemberManager.ADMIN_ID:
                    print('안됨.')
                elif self.ms.remove_member(id):
                    print('회원 강퇴.')
                else:
                    print('존재하지 않는 회원.')
            else:
                print('없는 메뉴.')

    def list_all_member(self):
        print(self.current_user)
        if self.current_user != MemberManager.ADMIN_ID:
            print('사용 권한 없음')
            return
        
        member_list = self.ms.list_members()
        if len(member_list) <= 1:
            print('가입한 회원 없음')
        else:
            for member in member_list[1:]:
                print(member)

    def start_member_menu(self):
        print('---------- 회원 메뉴 ----------')
        while True:
            menu = self.select_menu(MemberManager.member_menu)
            if menu == 0: # 로그아웃
                self.current_user = None
                print('로그아웃.')
                break
            elif menu == 1: # 내정보조회
                member = self.ms.view_member_info(self.current_user)
                print(member)
            elif menu == 2: # 내정보수정 
                org_pw = input('>> 기존 비밀번호 : ')
                new_pw = input('>> 새 비밀번호 : ')
                if self.ms.update_password(self.current_user, org_pw, new_pw):
                    print('비밀번호 수정.')
                else:
                    print('비밀번호 수정 실패.')
            elif menu == 3: # 회원탈퇴
                if self.ms.remove_member(self.current_user):
                    print('회원탈퇴 완료.')
                    self.current_user = None
                    break
                else:
                    print('회원탈퇴 실패.')
            else:
                print('없는 메뉴.')

    def show_welcome(self):
        print('=' * 50)
        title = 'Member Manager'
        print(f'{title:^50}')
        print('=' * 50)

    def say_goodbye(self):
        print('ㅃㅇ')

    def print_menu(self, menu_list):
        print('-' * 40)
        for i in range(1, len(menu_list)):
            print(f'{i}. {menu_list[i]}')
        print(f'0. {menu_list[0]}')
        print('-' * 40)

    def select_menu(self, menu_list):
        self.print_menu(menu_list)
        try:
            menu = int(input('메뉴 선택 : '))
            return menu
        except ValueError:
            return -1

if __name__ == '__main__':
    app = MemberManager()
    app.main()