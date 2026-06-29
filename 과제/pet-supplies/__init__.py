애완동물 용품샵 - 클래스다이어그램 기준 기능별 폴더 + DAO 구현본
==============================================================

이번 버전은 루트(petshop 바로 아래)에 중복 파일을 두지 않았습니다.
실제 코드 파일은 모두 기능 폴더 안에만 있습니다.

[폴더 구조]
petshop/
  members/       회원, 로그인/권한, MemberDAO
  products/      상품, ProductDAO
  carts/         장바구니, CartDAO
  orders/        주문, OrderDAO
  deliveries/    배송, DeliveryDAO

[추가된 DAO]
- MemberDAO
- ProductDAO
- CartDAO
- OrderDAO
- DeliveryDAO

[변경 내용]
- Manager 클래스 내부에서 직접 딕셔너리를 관리하던 부분을 DAO가 담당하도록 수정했습니다.
- Manager는 기능 처리, DAO는 저장/조회/수정/삭제 담당으로 분리했습니다.
- 클래스다이어그램에 맞춰 일부 별칭 메서드도 추가했습니다.
