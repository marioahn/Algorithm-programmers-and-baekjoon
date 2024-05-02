import java.util.Scanner;
public class Main {
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		int l = sc.nextInt();
		if(1 <= l % 5 && l % 5 <= 4) {
			System.out.println(l / 5 + 1);
		}else {
			System.out.println(l / 5);
		}
		sc.close();
	}
}