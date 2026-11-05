package bank.app.menu;

import bank.account.AccountService;
import bank.app.console.ConsoleMenu;
import bank.member.MemberService;

public class AdminMenu extends ConsoleMenu {

	protected AdminMenu(AccountService as, MemberService ms) {
		super(as, ms);
		menuList = new String[] {"로그아웃", "회원관리", "계좌관리"};
	}

	@Override
	public void run() {
		System.out.println("::: 관리자 메뉴 :::");
		while (true) {
			int menu = selectMenu();
			switch (menu) {
			case 1 -> new AdminMemberMenu(as, ms).run();//manageMembers();
			case 2 -> new AdminAccountMenu(as, ms).run(); //manageAccounts();
			case 0 -> {logout(); return;}
			default -> System.out.println("!! 메뉴에 있는 번호 선택 !!");
			}
		}
		
	}

	private void manageMembers() {
		System.out.println("::: 회원관리 :::");
	}

	private void manageAccounts() {
		System.out.println("::: 계좌관리 :::");
	}

	private void logout() {
		System.out.println("::: 로그아웃 :::");
		
	}

}
