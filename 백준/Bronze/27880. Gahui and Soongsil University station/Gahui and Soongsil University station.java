import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		int total = 0;
		
		for(int i = 0; i < 4; i++) {
			String a = sc.next();
			int b = sc.nextInt();
			if(a.equals("Es")) {
				total += b * 21;
			}else if(a.equals("Stair")) {
				total += b * 17;
			}
		}
		System.out.println(total);
		sc.close();
	}
}