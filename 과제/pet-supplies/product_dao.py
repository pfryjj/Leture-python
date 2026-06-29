from datetime import date
from .order import Order
from .order_item import OrderItem
from .order_dao import OrderDAO


class OrderManager:
    def __init__(self, cartMgr, productMgr, dao=None):
        self.__cartMgr = cartMgr
        self.__productMgr = productMgr
        self.__dao = dao if dao else OrderDAO()

    def createOrder(self, memberId):
        cart = self.__cartMgr.getCart(memberId)
        if cart.isEmpty():
            return None, '장바구니가 비어 있습니다.'

        for item in cart.get_items():
            product = self.__productMgr.getProduct(item.get_productNo())
            if not product:
                return None, f'{item.get_productName()} 상품이 존재하지 않습니다.'
            if product.get_stock() < item.get_quantity():
                return None, f'{product.get_name()} 재고가 부족합니다.'

        order_items = [
            OrderItem(item.get_productNo(), item.get_productName(), item.get_price(), item.get_quantity())
            for item in cart.get_items()
        ]
        order = Order(0, memberId, order_items, date.today().isoformat(), Order.STATUS_ORDERED)
        self.__dao.insert_order(order)

        for item in order_items:
            self.__productMgr.reduceStock(item.get_productNo(), item.get_quantity())
        self.__cartMgr.clearCart(memberId)
        return order, '주문이 완료되었습니다.'

    def listOrders(self, memberId):
        return self.__dao.get_orders_by_member(memberId)

    def listAllOrders(self):
        return self.__dao.get_all_orders()

    def getOrder(self, orderNo):
        return self.__dao.get_order(orderNo)

    def getOrderDetail(self, orderNo):
        return self.getOrder(orderNo)

    def cancelOrder(self, orderNo):
        order = self.getOrder(orderNo)
        if not order or order.get_status() == Order.STATUS_CANCELLED:
            return False
        for item in order.get_items():
            self.__productMgr.restoreStock(item.get_productNo(), item.get_quantity())
        order.set_status(Order.STATUS_CANCELLED)
        return self.__dao.update_order(order)

    def updateStatus(self, orderNo, status):
        order = self.getOrder(orderNo)
        if not order:
            return False
        order.set_status(status)
        return self.__dao.update_order(order)

    def getDao(self):
        return self.__dao

    def create_order(self, memberId): return self.createOrder(memberId)
    def list_orders(self, memberId): return self.listOrders(memberId)
    def list_all_orders(self): return self.listAllOrders()
    def get_order(self, orderNo): return self.getOrder(orderNo)
    def get_order_detail(self, orderNo): return self.getOrderDetail(orderNo)
    def cancel_order(self, orderNo): return self.cancelOrder(orderNo)
    def update_status(self, orderNo, status): return self.updateStatus(orderNo, status)
    def get_dao(self): return self.getDao()
