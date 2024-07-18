import java.util.Scanner;
public class Main {
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		for(int i = 0; i < n; i++) {
			int year = sc.nextInt();
			
			if((year + 1) % (year % 100) == 0) {
				System.out.println("Good");
			}else {
				System.out.println("Bye");
			}
		}
		sc.close();
	}
}