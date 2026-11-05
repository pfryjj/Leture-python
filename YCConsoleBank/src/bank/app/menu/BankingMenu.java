package bank.app.menu;

import bank.account.AccountService;
import bank.app.console.ConsoleMenu;
import bank.member.MemberService;

public class BankingMenu extends ConsoleMenu {
	protected BankingMenu(AccountService as, MemberService ms) {
		super(as, ms);
	}

	@Override
	public void run() {
		System.out.println("::: 관리자 메뉴 :::");
		while (true) {
			int menu = selectMenu();
			switch (menu) {
			case 1 -> showMyAccount();
			case 2 -> deposit();
			case 3 -> withdraw();
			case 4 -> createAccount();
			case 5 -> deleteAccount();
			case 0 -> {exit(); return;}
			default -> System.out.println("!! 메뉴에 있는 번호 선택 !!");
			}
		}
		
	}

	private void showMyAccount() {
		System.out.println("::: 계좌목록 :::");
	}

	private void deposit() {
		System.out.println("::: 입금 :::");
	}
	
	private void withdraw() {
		System.out.println("::: 출금 :::");
	}
	
	private void createAccount() {
		System.out.println("::: 계좌 생성 :::");
	}
	
	private void deleteAccount() {
		System.out.println("::: 계좌 해지 :::");
	}

	private void exit() {
		System.out.println("::: 돌아가기 :::");
		
	}

}
