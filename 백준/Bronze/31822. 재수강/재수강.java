import java.util.Scanner;
public class Main {
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		String a = sc.next();
		int b = sc.nextInt();
		
		int j, count = 0;
		for(int i = 0; i < b; i++) {
			String c = sc.next();
			for(j = 0; j < 5; j++) {
				if(a.charAt(j) != c.charAt(j)) {
					break;
				}
			}
			if(j == 5) {
				count++;
			}
		}
		System.out.println(count);
		sc.close();
	}
}