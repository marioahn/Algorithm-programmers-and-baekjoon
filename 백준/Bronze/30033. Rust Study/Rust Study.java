import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		int[] a = new int[n];
		int[] b = new int[n];
		
		int count = 0;
		for(int i = 0; i < a.length; i++) {
			a[i] = sc.nextInt();
		}
		
		for(int i = 0; i < b.length; i++) {
			b[i] = sc.nextInt();
			if(b[i] >= a[i]) {
				count++;
			}
		}
		System.out.println(count);
		sc.close();
	}
}