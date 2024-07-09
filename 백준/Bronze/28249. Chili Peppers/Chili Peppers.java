import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		int total = 0;
		
		for(int i = 0; i < n; i++) {
			String a = sc.next();
			if(a.equals("Poblano")) {
				total += 1500;
			}else if(a.equals("Mirasol")) {
				total += 6000;
			}else if(a.equals("Serrano")) {
				total += 15500;
			}else if(a.equals("Cayenne")) {
				total += 40000;
			}else if(a.equals("Thai")) {
				total += 75000;
			}else if(a.equals("Habanero")) {
				total += 125000;
			}
		}
		System.out.println(total);
		sc.close();
	}
}