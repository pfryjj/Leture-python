package bank.app;

import bank.account.AccountListDao;
import bank.account.AccountService;
import bank.account.YCAccountService;
import bank.app.menu.StartMenu;
import bank.member.YCMemberService;
import bank.member.MemberListDao;
import bank.member.MemberService;

public class YCConsoleBankApp {

	public static void main(String[] args) {
		MemberService ms = new YCMemberService(new MemberListDao());
		AccountService as = new YCAccountService(new AccountListDao());
		
		new StartMenu(as, ms).run();
	}
}
