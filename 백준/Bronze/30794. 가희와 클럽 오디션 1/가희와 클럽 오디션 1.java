import java.util.Scanner;
public class Main {
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		String a = sc.next();
		int score = 0;
		
		if(a.equals("miss")) {
			score = 0;
		}else if(a.equals("bad")) {
			score = n * 200;
		}else if(a.equals("cool")) {
			score = n * 400;
		}else if(a.equals("great")) {
			score = n * 600;
		}else if(a.equals("perfect")) {
			score = n * 1000;
		}
		
		System.out.println(score);
		sc.close();
	}
}
