클래스다이어그램 대비 현재 코드 확인
==================================

1. 루트 중복 파일 제거
- petshop 바로 아래에는 중복용 member.py, product.py 같은 파일을 두지 않았습니다.
- 실제 코드 파일은 모두 기능 폴더 안에만 있습니다.

2. 새로 구현한 DAO 클래스
- members/member_dao.py : MemberDAO
- products/product_dao.py : ProductDAO
- carts/cart_dao.py : CartDAO
- orders/order_dao.py : OrderDAO
- deliveries/delivery_dao.py : DeliveryDAO

3. Manager와 DAO 역할 분리
- Manager : 회원가입, 상품 검색, 장바구니 담기, 주문 취소 같은 기능 처리
- DAO : 데이터 저장, 조회, 수정, 삭제 처리

4. 클래스다이어그램에 맞춰 추가한 주요 메서드/상수
[Member]
- check_password(password)
- update_info(phone, address)

[Product]
- decrease_stock(qty)
- increase_stock(qty)

[Cart]
- get_item(item_no)
- add_item(item)
- remove_item(item_no)
- total()

[Order]
- STATUS_ORDERED
- STATUS_CANCELLED
- get_order_detail(order_no)

[Delivery]
- STATUS_READY
- STATUS_SHIPPING
- STATUS_DONE

5. 아직 코드에 없는 클래스
- PetShopApp
- MemberService, ProductService, CartService, OrderService, DeliveryService
  현재 코드는 Service 이름 대신 MemberManager, ProductManager, CartManager, OrderManager, DeliveryManager를 사용합니다.
