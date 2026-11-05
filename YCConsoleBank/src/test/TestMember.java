package test;

import java.util.List;

import bank.member.YCMemberService;
import bank.member.Member;
import bank.member.MemberDao;
import bank.member.MemberListDao;
import bank.member.MemberService;

public class TestMember {
	public static void main(String[] args) {
//		testMemberDao();
		testMemberService();
	}
	
	public static void testMemberService() {
		MemberService ms = new YCMemberService(new MemberListDao());
		
		System.out.println(">> 회원가입 및 목록조회");
		ms.join("curi", "1234", "큐리");
		ms.join("curi2", "1111", "큐리2");
		printMemberList(ms.getAllMembers());
		
		System.out.println(">> 로그인, 로그아웃");
		if (ms.login("curi2", "1111"))
			System.out.println(ms.getLoggedMember());
		ms.logout();
		System.out.println(ms.getLoggedMember());
		
		System.out.println(">> 회원 정보 보기");
		ms.login("admin", "1234");
		System.out.println(ms.getMemberInfo("curi"));
		
		System.out.println(">> 비밀번호 변경");
		ms.changePassword("curi2", "1234", "cccc");
		printMemberList(ms.getAllMembers());
	}
	
	public static void testMemberDao() {
		MemberDao mdao = new MemberListDao();
		// 회원 추가
		
		System.out.println(">>> 회원 추가 및 회원 목록");
		mdao.save(new Member("admin", "1234", "admin", null, null, Member.ADMIN));
		mdao.save(new Member("hyejeong", "1111", "이혜정", null, null, Member.USER));
		mdao.save(new Member("curi", "1111", "큐리", null, null, Member.USER));
		printMemberList(mdao.findAll());
		
		System.out.println(">>> id로 회원 찾기");
		Member m = mdao.findById("curi");
		System.out.println(m);
		
		System.out.println(">>> 비밀번호 변경");
		m.setPassword("1234");
		mdao.update(m);
		printMemberList(mdao.findAll());
		
		System.out.println(">>> 회원 삭제");
		mdao.delete(mdao.findById("curi"));
		printMemberList(mdao.findAll());

		
	}
	
	public static void printMemberList(List<Member> mlist) {
		for (Member m : mlist) {
			System.out.println(m);
		}
	}
}
