#======================
# 데이터 모델 정의 : Member
class Member:
    def __init__(self, id, password, name):
        self.__member_no = 0
        self.__id = id
        self.__password = password
        self.__name = name

    def get_member_no(self):
        return self.__member_no
    def get_id(self):
        return self.__id
    def get_password(self):
        return self.__password
    def get_name(self):
        return self.__name
    def set_password(self, password):
        self.__password = password
    def set_name(self, name):
        self.__name = name
    
    def __str__(self):
        return f'{self.__member_no}\t{self.__id}\t{self.__name}\t{self.__password}'   

#==================
# 회원 관리 서비스
class MemberService:
    def __init__(self, memberDao):
        self.__dao = memberDao

    def join(self, member):
        if self.__dao.is_exist(member.get_id()):
            return False
        self.__dao.insert_member(member)
        return True

    def login(self, id, password):
        member = self.__dao.get_member_info(id)
        if member:
            if password == member.get_password():
                return id
        return None
    
    def list_members(self):
        member_list = self.__dao.get_all_members()
        return member_list

    def view_member_info(self, id):
        return self.__dao.get_member_info(id)

    def update_member_info(self, id, update_type, update_data):
        member = self.__dao.get_member_info(id)
        if member:
            if update_type == "1":
                member.set_password(update_data)
            elif update_type == "2":
                member.set_name(update_data)
            else:
                return False
            self.__dao.update_member_info(id, member)
            return True
        return False

    def remove_member(self, id):
        if self.__dao.is_exist(id):
            self.__dao.remove_member(id)
            return True
        return False

#====================
# 회원 데이터 접근
class MemberDAO:
    def __init__(self):
        self.__memberDB = {}
    
    def insert_member(self, member):
        self.__memberDB[member.get_id()] = member

    def is_exist(self, id):
        if id in self.__memberDB.keys(): return True
        return False
    
    def get_member_info(self, id):
        if self.is_exist(id):
            return self.__memberDB[id]
        else:
            return None
        
    def get_all_members(self):
        if self.__memberDB:
            return list(self.__memberDB.values())

    def update_member_info(self, id, member):
        if self.is_exist(id):
            self.__memberDB[id] = member

    def remove_member(self, id):
        if self.is_exist(id):
            del self.__memberDB[id]