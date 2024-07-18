import java.util.Scanner;
public class Main {
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		int m = sc.nextInt();
		
		int totalCount = 0;
		for(int i = 0; i < n; i++) {
			String a = sc.next();
			int count = 0;
			for(int j = 0; j < a.length(); j++) {
				if(a.charAt(j) == 'O') {
					count++;
				}
			}
			
			if(count > m / 2) {
				totalCount++;
			}
		}
		System.out.println(totalCount);
		sc.close();
	}
}