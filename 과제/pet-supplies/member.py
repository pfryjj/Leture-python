class DeliveryDAO:
    def __init__(self):
        self.__deliveryDB = {}
        self.__next_no = 1

    def insert_delivery(self, delivery):
        if delivery.get_delivery_no() == 0:
            delivery.set_delivery_no(self.__next_no)
        self.__deliveryDB[delivery.get_order_no()] = delivery
        self.__next_no = max(self.__next_no, delivery.get_delivery_no() + 1)
        return True

    def get_delivery(self, order_no):
        return self.__deliveryDB.get(order_no)

    def get_all_deliveries(self):
        return list(self.__deliveryDB.values())

    def update_delivery(self, delivery):
        order_no = delivery.get_order_no()
        if order_no not in self.__deliveryDB:
            return False
        self.__deliveryDB[order_no] = delivery
        return True
