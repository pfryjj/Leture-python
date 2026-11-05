package bank.app.menu;

import bank.account.AccountService;
import bank.app.console.ConsoleMenu;
import bank.member.MemberService;

public class AdminAccountMenu extends ConsoleMenu {

	protected AdminAccountMenu(AccountService as, MemberService ms) {
		super(as, ms);
	}

	@Override
	public void run() {
		System.out.println("계좌 관리 메뉴");
		while (true) {
			int menu = selectMenu();
			switch (menu) {
			case 1 -> showAllAccounts();
			case 2 -> showMemberAccounts();
			case 0 -> {exit(); return;}
			default -> System.out.println("!! 메뉴에 있는 번호 선택 !!");
			}
		}
	}	
	private void showAllAccounts() {
		System.out.println("전체 계좌목록 조회");
	}
	private void showMemberAccounts() {
		System.out.println("회원별 계좌목록 조회");
	}
	private void exit() {
		System.out.println("돌아가기");
	}
}
