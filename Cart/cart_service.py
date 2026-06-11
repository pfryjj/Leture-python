from .cart import Cart

class CartService:
    def __init__(self):
        self.__carts = {}   # {owner_id: Cart}

    def get_cart(self, owner_id):
        if owner_id not in self.__carts:
            self.__carts[owner_id] = Cart(owner_id)
        return self.__carts[owner_id]

    def add_item(self, owner_id, book_no, qty=1):
        self.get_cart(owner_id).add_item(book_no, qty)

    def remove_item(self, owner_id, book_no):
        return self.get_cart(owner_id).remove_item(book_no)

    def clear(self, owner_id):
        self.get_cart(owner_id).clear()

    def get_total(self, owner_id, book_service):
        total = 0
        for book_no, qty in self.get_cart(owner_id).get_items().items():
            book = book_service.get_book(book_no)
            if book:
                total += book.get_price() * qty
        return total

    def checkout(self, owner_id, account_no, account_pw, book_service, account_service):
        cart = self.get_cart(owner_id)
        if cart.is_empty():
            return False, '장바구니가 비어 있습니다.'

        items = cart.get_items()

        for book_no, qty in items.items():
            book = book_service.get_book(book_no)
            if not book or book.get_quantity() < qty:
                name = book.get_title() if book else str(book_no)
                return False, f'재고 부족: {name}'

        total = self.get_total(owner_id, book_service)
        balance = account_service.get_balance(account_no)
        if balance is None:
            return False, '계좌를 찾을 수 없습니다.'
        if balance < total:
            return False, f'잔액 부족 (필요: {total:,}원, 현재: {balance:,}원)'

        if not account_service.withdraw(account_no, account_pw, total):
            return False, '출금에 실패하였습니다. (비밀번호 확인)'

        for book_no, qty in items.items():
            book_service.reduce_stock(book_no, qty)

        cart.clear()
        return True, f'결제 완료! {total:,}원이 출금되었습니다.'
