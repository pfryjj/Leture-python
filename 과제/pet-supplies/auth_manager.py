from datetime import date
from .delivery import Delivery
from .delivery_dao import DeliveryDAO


class DeliveryManager:
    STATUS_FLOW = [Delivery.STATUS_READY, Delivery.STATUS_SHIPPING, Delivery.STATUS_DONE]

    def __init__(self, dao=None):
        self.__dao = dao if dao else DeliveryDAO()

    def createDelivery(self, orderNo, address):
        delivery = self.__dao.get_delivery(orderNo)
        if delivery:
            return delivery
        delivery = Delivery(0, orderNo, address, Delivery.STATUS_READY, date.today().isoformat())
        self.__dao.insert_delivery(delivery)
        return delivery

    def getDelivery(self, orderNo):
        return self.__dao.get_delivery(orderNo)

    def listDeliveries(self):
        return self.__dao.get_all_deliveries()

    def updateStatus(self, orderNo, status):
        delivery = self.getDelivery(orderNo)
        if not delivery:
            return False, '해당 주문의 배송 정보가 없습니다.'
        if status not in DeliveryManager.STATUS_FLOW:
            return False, '잘못된 배송 상태입니다.'
        if delivery.get_status() == '배송취소':
            return False, '취소된 배송은 상태를 변경할 수 없습니다.'
        delivery.set_status(status)
        delivery.set_updatedDate(date.today().isoformat())
        self.__dao.update_delivery(delivery)
        return True, '배송 상태를 변경했습니다.'

    def cancelDelivery(self, orderNo):
        delivery = self.getDelivery(orderNo)
        if not delivery:
            return False, '해당 주문의 배송 정보가 없습니다.'
        if delivery.get_status() in (Delivery.STATUS_DONE, '배송취소'):
            return False, f'취소할 수 없는 상태입니다. (현재: {delivery.get_status()})'
        delivery.cancel()
        delivery.set_updatedDate(date.today().isoformat())
        self.__dao.update_delivery(delivery)
        return True, '배송을 취소했습니다.'

    def getDao(self):
        return self.__dao

    def create_delivery(self, orderNo, address): return self.createDelivery(orderNo, address)
    def get_delivery(self, orderNo): return self.getDelivery(orderNo)
    def view_delivery(self, orderNo): return self.getDelivery(orderNo)
    def list_deliveries(self): return self.listDeliveries()
    def update_status(self, orderNo, status): return self.updateStatus(orderNo, status)
    def cancel_delivery(self, orderNo): return self.cancelDelivery(orderNo)
    def get_dao(self): return self.getDao()
