# ======================
# 데이터 모델 정의 : Order
class Order:
    STATUS_ORDERED = '주문완료'
    STATUS_CANCELLED = '주문취소'

    def __init__(self, orderNo, memberId, items, orderDate, status='주문완료'):
        self.__orderNo = orderNo
        self.__memberId = memberId
        self.__items = items
        self.__orderDate = orderDate
        self.__status = status
        self.__totalPrice = sum(item.getSubtotal() for item in items)

    def get_orderNo(self): return self.__orderNo
    def get_order_no(self): return self.__orderNo
    def get_memberId(self): return self.__memberId
    def get_member_id(self): return self.__memberId
    def get_items(self): return list(self.__items)
    def get_orderDate(self): return self.__orderDate
    def get_order_date(self): return self.__orderDate
    def get_status(self): return self.__status
    def get_totalPrice(self): return self.__totalPrice
    def get_total_price(self): return self.__totalPrice
    def set_orderNo(self, orderNo): self.__orderNo = orderNo
    def set_order_no(self, orderNo): self.__orderNo = orderNo
    def set_status(self, status): self.__status = status

    def __str__(self):
        return (f'주문번호 : {self.__orderNo} | 회원아이디 : {self.__memberId} | '
                f'주문일 : {self.__orderDate} | 주문상태 : {self.__status} | '
                f'총금액 : {self.__totalPrice:,}원')
