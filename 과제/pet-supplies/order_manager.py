class MemberDAO:
    def __init__(self):
        self.__memberDB = {}

    def insert_member(self, member):
        member_id = member.get_id()
        if self.is_exist(member_id):
            return False
        self.__memberDB[member_id] = member
        return True

    def is_exist(self, id):
        return id in self.__memberDB

    def get_member(self, id):
        return self.__memberDB.get(id)

    def get_all_members(self):
        return list(self.__memberDB.values())

    def update_member(self, id, member):
        if not self.is_exist(id):
            return False
        self.__memberDB[id] = member
        return True

    def remove_member(self, id):
        if not self.is_exist(id):
            return False
        del self.__memberDB[id]
        return True
