import java.util.Scanner;
 
public class Main {
	public static void main(String[] args) {
 
		Scanner in = new Scanner(System.in);
 
		double R = in.nextDouble();	// 반지름 R
		in.close();
		
		System.out.println(R * R * Math.PI);
		System.out.println(2 * R * R);
	}
}