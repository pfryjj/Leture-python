# ======================
# 로그인/권한 확인 : AuthManager
class AuthManager:
    ADMIN_ID = 'admin'
    ADMIN_PASSWORD = 'admin1234'

    def __init__(self, memberMgr):
        self.__memberMgr = memberMgr
        self.__loginUser = None

    def login(self, id, pw):
        member = self.__memberMgr.getMember(id)
        if member and member.get_password() == pw:
            self.__loginUser = member
            return True
        return False

    def logout(self):
        self.__loginUser = None

    def checkRole(self, role):
        if not self.__loginUser:
            return False
        if role == 'admin':
            return self.__loginUser.is_admin()
        if role == 'member':
            return not self.__loginUser.is_admin()
        return False

    def authenticate(self):
        return self.__loginUser is not None

    def getLoginUser(self):
        return self.__loginUser

    # snake_case 별칭
    def check_role(self, role): return self.checkRole(role)
    def get_login_user(self): return self.getLoginUser()
