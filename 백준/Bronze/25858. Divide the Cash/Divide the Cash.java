import java.util.Scanner;
public class Main {
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		int d = sc.nextInt();
		int[] m = new int[n];
		int total = 0;
		
		for(int i = 0; i < n; i++) {
			m[i] = sc.nextInt();
			total += m[i];
		}
		
		total = d / total;
		for(int i = 0; i < n; i++) {
			System.out.println(total * m[i]);
		}
		sc.close();
	}
}