import java.util.Scanner;
public class Main {
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		String[] f = new String[n];
		
		for(int i = 0; i < f.length; i++) {
			f[i] = sc.next();
		}
		
		String h = sc.next();
		int count = 0;
		for(int i = 0; i < f.length; i++) {
			if(f[i].equals(h)) {
				count++;
			}
		}
		System.out.println(count);
		sc.close();
	}
}