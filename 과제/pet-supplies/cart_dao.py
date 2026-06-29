# ======================
# 데이터 모델 정의 : CartItem
class CartItem:
    def __init__(self, productNo, productName, price, quantity):
        self.__productNo = productNo
        self.__productName = productName
        self.__price = price
        self.__quantity = quantity

    def get_productNo(self): return self.__productNo
    def get_product_no(self): return self.__productNo
    def get_productName(self): return self.__productName
    def get_product_name(self): return self.__productName
    def get_price(self): return self.__price
    def get_quantity(self): return self.__quantity
    def set_quantity(self, quantity): self.__quantity = quantity

    def getSubtotal(self):
        return self.__price * self.__quantity

    def get_subtotal(self):
        return self.getSubtotal()

    def __str__(self):
        return (f'[{self.__productNo}] {self.__productName:<18} x {self.__quantity}개 '
                f'= {self.getSubtotal():,}원')
