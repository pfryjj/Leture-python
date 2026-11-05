package bank.app.menu;

import bank.account.AccountService;
import bank.app.console.ConsoleMenu;
import bank.member.MemberService;

public class MyInfoMenu extends ConsoleMenu {

	protected MyInfoMenu(AccountService as, MemberService ms) {
		super(as, ms);
	}

	@Override
	public void run() {
		System.out.println("계좌 관리 메뉴");
		while (true) {
			int menu = selectMenu();
			switch (menu) {
			case 1 -> changePassword();
			case 2 -> deleteMyAccount();
			case 0 -> {exit(); return;}
			default -> System.out.println("!! 메뉴에 있는 번호 선택 !!");
			}
		}
	}	
	private void changePassword() {
		System.out.println("비밀번호 변경");
	}
	private void deleteMyAccount() {
		System.out.println("회원 탈퇴");
	}
	private void exit() {
		System.out.println("돌아가기");
	}
}