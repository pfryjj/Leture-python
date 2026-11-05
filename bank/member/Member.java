package bank.member;

public class Member {

	private String id;
	private String password;
	private String name;
	private String email;
	private String moblie;
	
	public Member(String id, String password, String name, String email, String mobile) {
		this.id = id;
		this.password = password;
		this.name = name;
		this.email = email;
		this.moblie = mobile;
	}
	
	public Member(String id, String password, String name) {
		this(id, password, name, null, null);
		
	}
	
	public String getId() {
		return id;
	}
	public void setId(String id) {
		this.id = id;
	}
	public String getPassword() {
		return password;
	}
	public void setPassword(String password) {
		this.password = password;
	}
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public String getEmail() {
		return email;
	}
	public void setEmail(String email) {
		this.email = email;
	}
	public String getMoblie() {
		return moblie;
	}
	public void setMoblie(String moblie) {
		this.moblie = moblie;
	}

	@Override
	public String toString() {
		return "[" + id + ", " + password + ", " + name + ", " + email + ", "
				+ moblie + "]";
	}
	
	
}
