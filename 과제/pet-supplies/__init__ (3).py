# ======================
# 데이터 모델 정의 : Delivery
class Delivery:
    STATUS_READY = '배송준비'
    STATUS_SHIPPING = '배송중'
    STATUS_DONE = '배송완료'

    def __init__(self, deliveryNo, orderNo, address, status='배송준비', updatedDate=''):
        self.__deliveryNo = deliveryNo
        self.__orderNo = orderNo
        self.__address = address
        self.__status = status
        self.__updatedDate = updatedDate

    def get_deliveryNo(self): return self.__deliveryNo
    def get_delivery_no(self): return self.__deliveryNo
    def get_orderNo(self): return self.__orderNo
    def get_order_no(self): return self.__orderNo
    def get_address(self): return self.__address
    def get_status(self): return self.__status
    def get_updatedDate(self): return self.__updatedDate
    def get_updated_date(self): return self.__updatedDate

    def set_deliveryNo(self, deliveryNo): self.__deliveryNo = deliveryNo
    def set_delivery_no(self, deliveryNo): self.__deliveryNo = deliveryNo
    def set_status(self, status): self.__status = status
    def set_address(self, address): self.__address = address
    def set_updatedDate(self, updatedDate): self.__updatedDate = updatedDate

    def cancel(self):
        self.__status = '배송취소'

    def __str__(self):
        return (f'배송번호 : {self.__deliveryNo} | 주문번호 : {self.__orderNo} | '
                f'배송지 : {self.__address} | 배송상태 : {self.__status} | '
                f'갱신일 : {self.__updatedDate}')
