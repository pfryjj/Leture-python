from Member.member import Member
from Member.member_dao import MemberDAO
from Member.member_service import MemberService
from Account.account_dao import AccountDAO
from Account.account_service import AccountService
from book.book import Book
from book.book_dao import BookDAO
from book.book_service import BookService
from Cart.cart_service import CartService


class BookstoreApp:
    start_menu         = ['종료',    '로그인', '회원가입', '도서 목록']
    member_menu        = ['로그아웃', '도서 목록', '도서 검색', '장바구니', '주문 내역', '계좌 관리', '내 정보']
    cart_menu          = ['뒤로',    '장바구니 목록', '도서 담기', '항목 삭제', '결제']
    banking_menu       = ['뒤로',    '계좌 개설', '잔액 조회', '입금', '출금', '이체']
    member_myinfo_menu = ['뒤로',    '내 정보 조회', '비밀번호 변경', '회원 탈퇴']
    admin_menu         = ['로그아웃', '도서 관리', '회원 관리', '계좌 관리']
    admin_book_menu    = ['뒤로',    '도서 목록', '도서 등록', '도서 삭제']
    admin_member_menu  = ['뒤로',    '회원 목록', '회원 정보 조회', '회원 강제 탈퇴']
    admin_account_menu = ['뒤로',    '전체 계좌 조회']

    def __init__(self):
        self.msv = MemberService(MemberDAO())
        self.asv = AccountService(AccountDAO())
        self.bsv = BookService(BookDAO())
        self.csv = CartService()
        self.__orders = []   # [(owner_id, [title x qty, ...], total)]
        self.__init_sample_books()

    def __init_sample_books(self):
        samples = [
            Book('파이썬 프로그래밍', '홍길동', 25000, 10),
            Book('자바 완전정복',     '이순신', 30000,  5),
            Book('웹 개발의 정석',   '강감찬', 28000,  8),
            Book('알고리즘 기초',    '세종대왕', 22000, 15),
            Book('데이터베이스 입문', '유관순', 27000,  3),
        ]
        for b in samples:
            self.bsv.add_book(b)

    # ----------------------------------------------------------
    # 공통 UI 헬퍼
    # ----------------------------------------------------------
    def _print_menu(self, menu_list, title=None):
        print('-' * 44)
        if title:
            print(f'  {title}')
            print('-' * 44)
        for i in range(1, len(menu_list)):
            print(f'  {i}. {menu_list[i]}')
        print(f'  0. {menu_list[0]}')
        print('-' * 44)

    def _select_menu(self, menu_list, title=None):
        self._print_menu(menu_list, title)
        try:
            return int(input('메뉴 선택 : '))
        except ValueError:
            return -1

    def _header(self, title):
        print(f'\n{"=" * 44}')
        print(f'  {title}')
        print('=' * 44)

    # ----------------------------------------------------------
    # 1. 도서 관련
    # ----------------------------------------------------------
    def view_book_list(self):
        self._header('도서 목록')
        books = self.bsv.list_books()
        if not books:
            print('  등록된 도서가 없습니다.')
            return
        print(f'  {"번호":>4}  {"제목":<20} {"저자":<10} {"가격":>8}  {"재고":>4}')
        print('  ' + '-' * 52)
        for b in books:
            print(f'  [{b.get_book_no():>3}] {b.get_title():<20} {b.get_author():<10}'
                  f' {b.get_price():>8,}원  {b.get_quantity():>3}권')

    def search_book(self):
        self._header('도서 검색')
        print('  1. 제목 검색   2. 저자 검색')
        try:
            mode = int(input('선택 : '))
        except ValueError:
            return
        keyword = input('검색어 : ').strip()
        results = (self.bsv.search_by_title(keyword) if mode == 1
                   else self.bsv.search_by_author(keyword))
        if not results:
            print('  검색 결과가 없습니다.')
        else:
            for b in results:
                print(f'  {b}')

    # ----------------------------------------------------------
    # 2. 시작 메뉴 / 로그인 / 회원가입
    # ----------------------------------------------------------
    def show_start_menu(self):
        while True:
            menu = self._select_menu(BookstoreApp.start_menu, '온라인 서점')
            if menu == 0:
                break
            elif menu == 1:
                self.login()
            elif menu == 2:
                self.register_member()
            elif menu == 3:
                self.view_book_list()
            else:
                print('  없는 메뉴입니다.')

    def login(self):
        self._header('로그인')
        id_ = input('>> ID       : ').strip()
        pw  = input('>> 비밀번호 : ').strip()
        if self.msv.login(id_, pw):
            print(f'\n  {id_}님, 환영합니다!')
            if id_ == MemberService.ADMIN_ID:
                self.show_admin_menu()
            else:
                self._member_menu()
        else:
            print('  로그인에 실패하였습니다.')

    def register_member(self):
        self._header('회원가입')
        id_  = input('>> ID       : ').strip()
        pw   = input('>> 비밀번호 : ').strip()
        name = input('>> 이름     : ').strip()
        if self.msv.join(Member(id_, pw, name)):
            print('  회원가입이 완료되었습니다.')
        else:
            print('  이미 사용 중인 ID입니다.')

    # ----------------------------------------------------------
    # 3. 회원 메뉴
    # ----------------------------------------------------------
    def _member_menu(self):
        while True:
            menu = self._select_menu(BookstoreApp.member_menu,
                                     f'[ {self.msv.current_user} ] 회원 메뉴')
            if menu == 0:
                self.msv.logout()
                print('  로그아웃되었습니다.')
                break
            elif menu == 1:
                self.view_book_list()
            elif menu == 2:
                self.search_book()
            elif menu == 3:
                self._cart_menu()
            elif menu == 4:
                self.view_order_history()
            elif menu == 5:
                self.show_banking_menu()
            elif menu == 6:
                self.show_member_myinfo()
            else:
                print('  없는 메뉴입니다.')

    def show_member_myinfo(self):
        while True:
            menu = self._select_menu(BookstoreApp.member_myinfo_menu, '내 정보')
            if menu == 0:
                break
            elif menu == 1:
                m = self.msv.view_member_info(self.msv.current_user)
                if m:
                    print(f'\n  {m}')
            elif menu == 2:
                self._change_password()
            elif menu == 3:
                if self._remove_self():
                    return
            else:
                print('  없는 메뉴입니다.')

    def _change_password(self):
        old = input('기존 비밀번호 : ').strip()
        new = input('새  비밀번호  : ').strip()
        if self.msv.update_member_password(self.msv.current_user, old, new):
            print('  비밀번호가 변경되었습니다.')
        else:
            print('  변경에 실패하였습니다. (기존 비밀번호 확인)')

    def _remove_self(self):
        if input('정말 탈퇴하시겠습니까? (y/n) : ').strip().lower() == 'y':
            if self.msv.remove_member(self.msv.current_user):
                print('  탈퇴 처리되었습니다.')
                self.msv.logout()
                return True
        return False

    # ----------------------------------------------------------
    # 4. 장바구니
    # ----------------------------------------------------------
    def _cart_menu(self):
        while True:
            menu = self._select_menu(BookstoreApp.cart_menu, '장바구니')
            if menu == 0:
                break
            elif menu == 1:
                self.view_cart()
            elif menu == 2:
                self.add_to_cart()
            elif menu == 3:
                self._remove_from_cart()
            elif menu == 4:
                self.order_book()
            else:
                print('  없는 메뉴입니다.')

    def add_to_cart(self):
        self.view_book_list()
        try:
            book_no = int(input('담을 도서 번호 : '))
            qty     = int(input('수량           : '))
        except ValueError:
            print('  올바른 값을 입력하세요.')
            return
        book = self.bsv.get_book(book_no)
        if not book:
            print('  존재하지 않는 도서입니다.')
            return
        if book.get_quantity() < qty:
            print(f'  재고 부족 (현재 재고: {book.get_quantity()}권)')
            return
        self.csv.add_item(self.msv.current_user, book_no, qty)
        print(f'  [{book.get_title()}] {qty}권을 장바구니에 담았습니다.')

    def view_cart(self):
        self._header('장바구니 목록')
        items = self.csv.get_cart(self.msv.current_user).get_items()
        if not items:
            print('  장바구니가 비어 있습니다.')
            return
        total = 0
        for book_no, qty in items.items():
            book = self.bsv.get_book(book_no)
            if book:
                sub = book.get_price() * qty
                total += sub
                print(f'  [{book_no}] {book.get_title():<20} x {qty}권  {sub:,}원')
        print(f'  {"합계":>35} {total:,}원')

    def _remove_from_cart(self):
        self.view_cart()
        try:
            book_no = int(input('삭제할 도서 번호 : '))
        except ValueError:
            return
        if self.csv.remove_item(self.msv.current_user, book_no):
            print('  삭제되었습니다.')
        else:
            print('  장바구니에 없는 도서입니다.')

    def order_book(self):
        self._header('결제')
        self.view_cart()
        if self.csv.get_cart(self.msv.current_user).is_empty():
            return
        total = self.csv.get_total(self.msv.current_user, self.bsv)
        print(f'\n  결제 금액: {total:,}원')
        account_no = input('계좌번호      : ').strip()
        account_pw = input('계좌 비밀번호 : ').strip()
        items_snapshot = self.csv.get_cart(self.msv.current_user).get_items()
        ok, msg = self.csv.checkout(self.msv.current_user, account_no, account_pw,
                                    self.bsv, self.asv)
        print(f'  {msg}')
        if ok:
            desc = [f'{self.bsv.get_book(no).get_title()} x{q}'
                    for no, q in items_snapshot.items()
                    if self.bsv.get_book(no)]
            self.__orders.append((self.msv.current_user, desc, total))

    def view_order_history(self):
        self._header('주문 내역')
        my = [o for o in self.__orders if o[0] == self.msv.current_user]
        if not my:
            print('  주문 내역이 없습니다.')
            return
        for i, (_, titles, total) in enumerate(my, 1):
            print(f'  [{i}] {", ".join(titles)}  /  {total:,}원')

    # ----------------------------------------------------------
    # 5. 계좌 (뱅킹)
    # ----------------------------------------------------------
    def show_banking_menu(self):
        while True:
            menu = self._select_menu(BookstoreApp.banking_menu, '계좌 관리')
            if menu == 0:
                break
            elif menu == 1:
                self._create_account()
            elif menu == 2:
                self._view_balance()
            elif menu == 3:
                self._deposit()
            elif menu == 4:
                self._withdraw()
            elif menu == 5:
                self._transfer()
            else:
                print('  없는 메뉴입니다.')

    def _create_account(self):
        self._header('계좌 개설')
        no    = input('계좌번호 (전화번호) : ').strip()
        owner = input('예금주             : ').strip()
        try:
            balance = int(input('초기 입금액        : '))
        except ValueError:
            print('  올바른 금액을 입력하세요.')
            return
        pw = input('계좌 비밀번호       : ').strip()
        if self.asv.create_account(no, owner, balance, pw):
            print(f'  계좌가 개설되었습니다. (계좌번호: {no})')
        else:
            print('  이미 존재하는 계좌번호입니다.')

    def _view_balance(self):
        no = input('계좌번호 : ').strip()
        bal = self.asv.get_balance(no)
        print(f'  잔액: {bal:,}원' if bal is not None else '  계좌를 찾을 수 없습니다.')

    def _deposit(self):
        no = input('계좌번호 : ').strip()
        try:
            amount = int(input('입금액   : '))
        except ValueError:
            return
        if self.asv.deposit(no, amount):
            print(f'  {amount:,}원 입금 완료. 잔액: {self.asv.get_balance(no):,}원')
        else:
            print('  계좌를 찾을 수 없습니다.')

    def _withdraw(self):
        no = input('계좌번호 : ').strip()
        pw = input('비밀번호 : ').strip()
        try:
            amount = int(input('출금액   : '))
        except ValueError:
            return
        if self.asv.withdraw(no, pw, amount):
            print(f'  {amount:,}원 출금 완료. 잔액: {self.asv.get_balance(no):,}원')
        else:
            print('  출금 실패 (잔액 부족 또는 비밀번호 오류)')

    def _transfer(self):
        from_no = input('출금 계좌번호 : ').strip()
        pw      = input('비밀번호      : ').strip()
        to_no   = input('입금 계좌번호 : ').strip()
        try:
            amount = int(input('이체 금액     : '))
        except ValueError:
            return
        if self.asv.transfer(from_no, pw, to_no, amount):
            print(f'  이체 완료. 잔액: {self.asv.get_balance(from_no):,}원')
        else:
            print('  이체 실패 (잔액 부족 또는 비밀번호 오류)')

    # ----------------------------------------------------------
    # 6. 관리자 메뉴
    # ----------------------------------------------------------
    def show_admin_menu(self):
        while True:
            menu = self._select_menu(BookstoreApp.admin_menu, '관리자 메뉴')
            if menu == 0:
                self.msv.logout()
                print('  로그아웃되었습니다.')
                break
            elif menu == 1:
                self._admin_book_menu()
            elif menu == 2:
                self.manage_admin_member()
            elif menu == 3:
                self.manage_admin_account()
            else:
                print('  없는 메뉴입니다.')

    def _admin_book_menu(self):
        while True:
            menu = self._select_menu(BookstoreApp.admin_book_menu, '도서 관리')
            if menu == 0:
                break
            elif menu == 1:
                self.view_book_list()
            elif menu == 2:
                self._admin_add_book()
            elif menu == 3:
                self._admin_remove_book()
            else:
                print('  없는 메뉴입니다.')

    def _admin_add_book(self):
        self._header('도서 등록')
        title  = input('제목 : ').strip()
        author = input('저자 : ').strip()
        try:
            price = int(input('가격 : '))
            qty   = int(input('수량 : '))
        except ValueError:
            print('  올바른 값을 입력하세요.')
            return
        self.bsv.add_book(Book(title, author, price, qty))
        print('  도서가 등록되었습니다.')

    def _admin_remove_book(self):
        self.view_book_list()
        try:
            book_no = int(input('삭제할 도서 번호 : '))
        except ValueError:
            return
        if self.bsv.remove_book(book_no):
            print('  도서가 삭제되었습니다.')
        else:
            print('  존재하지 않는 도서 번호입니다.')

    def manage_admin_member(self):
        while True:
            menu = self._select_menu(BookstoreApp.admin_member_menu, '회원 관리')
            if menu == 0:
                break
            elif menu == 1:
                self._header('회원 목록')
                members = self.msv.list_members()
                normals = [m for m in members if m.get_id() != MemberService.ADMIN_ID]
                if not normals:
                    print('  가입한 회원이 없습니다.')
                else:
                    for m in normals:
                        print(f'  {m}')
            elif menu == 2:
                id_ = input('>> ID : ').strip()
                m = self.msv.view_member_info(id_)
                print(f'  {m}' if m else '  없는 ID입니다.')
            elif menu == 3:
                id_ = input('>> ID : ').strip()
                if self.msv.remove_member(id_):
                    print('  탈퇴 처리되었습니다.')
                else:
                    print('  탈퇴 처리에 실패하였습니다.')
            else:
                print('  없는 메뉴입니다.')

    def manage_admin_account(self):
        while True:
            menu = self._select_menu(BookstoreApp.admin_account_menu, '계좌 관리')
            if menu == 0:
                break
            elif menu == 1:
                self._header('전체 계좌 목록')
                accounts = self.asv.get_all_accounts()
                if not accounts:
                    print('  등록된 계좌가 없습니다.')
                else:
                    for ac in accounts:
                        print(f'  {ac}')
            else:
                print('  없는 메뉴입니다.')

    # ----------------------------------------------------------
    # 메인 실행
    # ----------------------------------------------------------
    def run(self):
        print('=' * 44)
        print(f'{"온라인 서점":^40}')
        print('=' * 44)
        self.show_start_menu()
        print('\n  이용해 주셔서 감사합니다.')


if __name__ == '__main__':
    app = BookstoreApp()
    app.run()
