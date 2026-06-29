from datetime import date
from .member import Member
from .member_dao import MemberDAO


class MemberManager:
    def __init__(self, dao=None):
        self.__dao = dao if dao else MemberDAO()
        admin = Member('admin', 'admin1234', '관리자', '010-0000-0000', '본사',
                       date.today().isoformat(), True)
        self.__dao.insert_member(admin)

    def join(self, member):
        if self.__dao.is_exist(member.get_id()):
            return False
        if not member.get_joinDate():
            member.set_joinDate(date.today().isoformat())
        return self.__dao.insert_member(member)

    def getMember(self, id):
        return self.__dao.get_member(id)

    def listMembers(self):
        return self.__dao.get_all_members()

    def updateMemberInfo(self, id, phone, address):
        member = self.getMember(id)
        if not member:
            return False
        member.update_info(phone, address)
        return self.__dao.update_member(id, member)

    def deleteMember(self, id):
        if id == 'admin':
            return False
        return self.__dao.remove_member(id)

    def getDao(self):
        return self.__dao

    def get_member(self, id): return self.getMember(id)
    def list_members(self): return self.listMembers()
    def update_member_info(self, id, phone, address): return self.updateMemberInfo(id, phone, address)
    def delete_member(self, id): return self.deleteMember(id)
    def get_dao(self): return self.getDao()
