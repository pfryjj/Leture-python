class Book:
    def __init__(self, title, author, price, quantity=0):
        self.__book_no = 0
        self.__title = title
        self.__author = author
        self.__price = price
        self.__quantity = quantity

    def get_book_no(self): return self.__book_no
    def get_title(self): return self.__title
    def get_author(self): return self.__author
    def get_price(self): return self.__price
    def get_quantity(self): return self.__quantity

    def set_book_no(self, no): self.__book_no = no
    def set_title(self, title): self.__title = title
    def set_price(self, price): self.__price = price
    def set_quantity(self, qty): self.__quantity = qty

    def __str__(self):
        return (f'[{self.__book_no:>3}] {self.__title:<20} {self.__author:<10}'
                f' {self.__price:>8,}원  재고:{self.__quantity:>3}권')
