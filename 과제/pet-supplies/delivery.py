from .cart import Cart


class CartDAO:
    def __init__(self):
        self.__cartDB = {}

    def create_cart(self, member_id):
        if member_id not in self.__cartDB:
            self.__cartDB[member_id] = Cart(member_id)
        return self.__cartDB[member_id]

    def get_cart(self, member_id):
        return self.__cartDB.get(member_id)

    def save_cart(self, cart):
        self.__cartDB[cart.get_member_id()] = cart
        return True

    def remove_cart(self, member_id):
        if member_id not in self.__cartDB:
            return False
        del self.__cartDB[member_id]
        return True
