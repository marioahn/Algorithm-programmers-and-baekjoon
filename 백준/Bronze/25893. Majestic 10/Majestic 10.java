import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		
		for(int i = 0; i < n; i++) {
			int a = sc.nextInt();
			int b = sc.nextInt();
			int c = sc.nextInt();
			
			System.out.println(a + " " + b + " " + c);
			if(a < 10 && b < 10 && c < 10) {
				System.out.println("zilch");
			}else if(a >= 10 && b >= 10 && c >= 10) {
				System.out.println("triple-double");
			}else if(a >= 10 && b < 10 && c < 10 || b >= 10 && a < 10 && c < 10 || c >= 10 && a < 10 && b < 10) {
				System.out.println("double");
			}else {
				System.out.println("double-double");
			}
			System.out.println();
		}
		sc.close();
	}
}