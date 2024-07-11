import java.util.Scanner;
public class Main {
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		String a = sc.next();
		int count = 0;
		
		for(int i = 0; i < a.length() - 3; i++) {
			if(a.charAt(i) == 'D' && a.charAt(i + 1) == 'K' && a.charAt(i + 2) == 'S' && a.charAt(i + 3) == 'H') {
				count++;
			}
		}
		
		System.out.println(count);
		sc.close();
	}
}