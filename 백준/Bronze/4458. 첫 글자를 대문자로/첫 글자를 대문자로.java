import java.util.Scanner;
public class Main {
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		sc.nextLine();
		for(int i = 0; i < n; i++) {
			String a = sc.nextLine();
			if('a' <= a.charAt(0) && a.charAt(0) <= 'z') {
				System.out.print((char)(a.charAt(0) - 32));
			}else if('A' <= a.charAt(0) && a.charAt(0) <= 'Z') {
				System.out.print((char)(a.charAt(0)));
			}
			
			for(int j = 1; j < a.length(); j++) {
				System.out.print(a.charAt(j));
			}
			System.out.println();
		}
		sc.close();
	}
}
