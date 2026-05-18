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





