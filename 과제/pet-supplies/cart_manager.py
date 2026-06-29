# ======================
# 데이터 모델 정의 : Cart
from .cart_item import CartItem


class Cart:
    def __init__(self, memberId):
        self.__memberId = memberId
        self.__items = []

    def get_memberId(self): return self.__memberId
    def get_member_id(self): return self.__memberId
    def get_items(self): return list(self.__items)

    def get_item(self, item_no):
        for item in self.__items:
            if item.get_product_no() == item_no:
                return item
        return None

    def add_item(self, item):
        for cart_item in self.__items:
            if cart_item.get_product_no() == item.get_product_no():
                cart_item.set_quantity(cart_item.get_quantity() + item.get_quantity())
                return
        self.__items.append(item)

    def remove_item(self, item_no):
        return self.removeItem(item_no)

    def total(self):
        return self.getTotal()

    def addItem(self, product, qty):
        for item in self.__items:
            if item.get_productNo() == product.get_productNo():
                item.set_quantity(item.get_quantity() + qty)
                return
        self.__items.append(CartItem(product.get_productNo(), product.get_name(), product.get_price(), qty))

    def updateQty(self, productNo, qty):
        for item in self.__items:
            if item.get_productNo() == productNo:
                item.set_quantity(qty)
                return True
        return False

    def removeItem(self, productNo):
        for item in list(self.__items):
            if item.get_productNo() == productNo:
                self.__items.remove(item)
                return True
        return False

    def clear(self):
        self.__items = []

    def isEmpty(self):
        return len(self.__items) == 0

    def is_empty(self):
        return self.isEmpty()

    def getTotal(self):
        return sum(item.getSubtotal() for item in self.__items)
