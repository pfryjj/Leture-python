package bank.member;

import java.util.List;

public interface MemberDao {
	
	boolean save(Member m);
	List<Member> findAll();
	Member findById(String id);
	boolean update(Member m);
	boolean delete(Member m);
}
