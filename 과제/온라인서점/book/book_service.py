class BookService:
    def __init__(self, dao):
        self.dao = dao

    def add_book(self, book):
        return self.dao.insert(book)

    def list_books(self):
        return self.dao.get_all()

    def get_book(self, book_no):
        return self.dao.get(book_no)

    def search_by_title(self, keyword):
        return self.dao.search_title(keyword)

    def search_by_author(self, keyword):
        return self.dao.search_author(keyword)

    def reduce_stock(self, book_no, qty=1):
        book = self.dao.get(book_no)
        if not book or book.get_quantity() < qty:
            return False
        book.set_quantity(book.get_quantity() - qty)
        return True

    def remove_book(self, book_no):
        return self.dao.delete(book_no)
