import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		int[] a = new int[n];
		
		for(int i = 0; i < n; i++) {
			int b = sc.nextInt();
			int c = sc.nextInt();
			a[i] = b * c;
		}
		
		int max = a[0];
		for(int i = 1; i < n; i++) {
			max = Math.max(max, a[i]);
		}
		
		System.out.println(max);
		sc.close();
	}
}