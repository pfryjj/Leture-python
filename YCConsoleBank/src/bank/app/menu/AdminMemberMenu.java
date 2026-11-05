package bank.app.menu;

import bank.account.AccountService;
import bank.app.console.ConsoleMenu;
import bank.member.MemberService;

public class AdminMemberMenu extends ConsoleMenu {

	protected AdminMemberMenu(AccountService as, MemberService ms) {
		super(as, ms);
	}

	@Override
	public void run() {
		System.out.println("계좌 관리 메뉴");
		while (true) {
			int menu = selectMenu();
			switch (menu) {
			case 1 -> showAllMembers();
			case 2 -> deleteMember();
			case 0 -> {exit(); return;}
			default -> System.out.println("!! 메뉴에 있는 번호 선택 !!");
			}
		}
	}	
	private void showAllMembers() {
		System.out.println("회원 목록");
	}
	private void deleteMember() {
		System.out.println("회원 강퇴");
	}
	private void exit() {
		System.out.println("돌아가기");
	}
}