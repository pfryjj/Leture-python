# ======================
# 데이터 모델 정의 : Member
class Member:
    def __init__(self, id, password, name, phone='', address='', joinDate='', admin=False):
        self.__id = id
        self.__password = password
        self.__name = name
        self.__phone = phone
        self.__address = address
        self.__joinDate = joinDate
        self.__admin = admin

    def get_id(self): return self.__id
    def get_password(self): return self.__password
    def get_name(self): return self.__name
    def get_phone(self): return self.__phone
    def get_address(self): return self.__address
    def get_joinDate(self): return self.__joinDate
    def get_join_date(self): return self.__joinDate
    def is_admin(self): return self.__admin

    def check_password(self, password):
        return self.__password == password

    def update_info(self, phone, address):
        self.__phone = phone
        self.__address = address

    def set_password(self, password): self.__password = password
    def set_phone(self, phone): self.__phone = phone
    def set_address(self, address): self.__address = address
    def set_joinDate(self, joinDate): self.__joinDate = joinDate
    def set_admin(self, admin): self.__admin = admin

    def __str__(self):
        role = '관리자' if self.__admin else '회원'
        return (f'아이디 : {self.__id} | 이름 : {self.__name} | 전화번호 : {self.__phone} | '
                f'주소 : {self.__address} | 가입일 : {self.__joinDate} | 권한 : {role}')
