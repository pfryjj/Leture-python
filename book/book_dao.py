class BookDAO:
    _seq = 1

    def __init__(self):
        self.__db = {}

    def insert(self, book):
        book.set_book_no(BookDAO._seq)
        BookDAO._seq += 1
        self.__db[book.get_book_no()] = book
        return True

    def is_exist(self, book_no):
        return book_no in self.__db

    def get(self, book_no):
        return self.__db.get(book_no)

    def get_all(self):
        return list(self.__db.values())

    def search_title(self, keyword):
        return [b for b in self.__db.values() if keyword in b.get_title()]

    def search_author(self, keyword):
        return [b for b in self.__db.values() if keyword in b.get_author()]

    def update(self, book_no, book):
        if self.is_exist(book_no):
            self.__db[book_no] = book
            return True
        return False

    def delete(self, book_no):
        if self.is_exist(book_no):
            del self.__db[book_no]
            return True
        return False
