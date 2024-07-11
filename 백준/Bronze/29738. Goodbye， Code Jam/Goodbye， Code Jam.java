import java.util.Scanner;
public class Main {
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		
		for(int i = 0; i < n; i++) {
			int a = sc.nextInt();
			
			System.out.print("Case #" + (i + 1) + ": ");
			if(a > 4500) {
				System.out.println("Round 1");
			}else if(a > 1000) {
				System.out.println("Round 2");
			}else if(a > 25) {
				System.out.println("Round 3");
			}else {
				System.out.println("World Finals");
			}
		}
		sc.close();
	}
}