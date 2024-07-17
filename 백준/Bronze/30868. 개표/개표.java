import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		
		for(int i = 0; i < n; i++) {
			int m = sc.nextInt();
			int count5 = m / 5;
			int remainder5 = m % 5;
			
			for(int j = 0; j < count5; j++) {
				System.out.print("++++ ");
			}
			for(int j = 0; j < remainder5; j++) {
				System.out.print("|");
			}
			System.out.println();
		}
		sc.close();
	}
}