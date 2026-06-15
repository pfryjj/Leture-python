class Cart:
    def __init__(self, owner_id):
        self.__owner_id = owner_id
        self.__items = {}   # {book_no: quantity}

    def get_owner_id(self): return self.__owner_id
    def get_items(self): return dict(self.__items)

    def add_item(self, book_no, qty=1):
        self.__items[book_no] = self.__items.get(book_no, 0) + qty

    def remove_item(self, book_no):
        if book_no in self.__items:
            del self.__items[book_no]
            return True
        return False

    def clear(self):
        self.__items = {}

    def is_empty(self):
        return not self.__items
