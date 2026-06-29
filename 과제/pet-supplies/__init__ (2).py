from .cart_dao import CartDAO


class CartManager:
    def __init__(self, productMgr, dao=None):
        self.__productMgr = productMgr
        self.__dao = dao if dao else CartDAO()

    def getCart(self, memberId):
        cart = self.__dao.get_cart(memberId)
        if not cart:
            cart = self.__dao.create_cart(memberId)
        return cart

    def addItem(self, memberId, productNo, qty):
        product = self.__productMgr.getProduct(productNo)
        if not product:
            return False, '존재하지 않는 상품입니다.'
        if product.get_stock() < qty:
            return False, f'재고 부족 (현재 재고: {product.get_stock()}개)'
        cart = self.getCart(memberId)
        cart.addItem(product, qty)
        self.__dao.save_cart(cart)
        return True, '장바구니에 담았습니다.'

    def updateQty(self, memberId, productNo, qty):
        product = self.__productMgr.getProduct(productNo)
        if product and product.get_stock() < qty:
            return False
        cart = self.getCart(memberId)
        result = cart.updateQty(productNo, qty)
        if result:
            self.__dao.save_cart(cart)
        return result

    def removeItem(self, memberId, productNo):
        cart = self.getCart(memberId)
        result = cart.removeItem(productNo)
        if result:
            self.__dao.save_cart(cart)
        return result

    def clearCart(self, memberId):
        cart = self.getCart(memberId)
        cart.clear()
        self.__dao.save_cart(cart)

    def removeCart(self, memberId):
        return self.__dao.remove_cart(memberId)

    def getDao(self):
        return self.__dao

    def get_cart(self, memberId): return self.getCart(memberId)
    def add_item(self, memberId, productNo, qty): return self.addItem(memberId, productNo, qty)
    def update_qty(self, memberId, productNo, qty): return self.updateQty(memberId, productNo, qty)
    def remove_item(self, memberId, productNo): return self.removeItem(memberId, productNo)
    def clear_cart(self, memberId): return self.clearCart(memberId)
    def remove_cart(self, memberId): return self.removeCart(memberId)
    def get_dao(self): return self.getDao()
