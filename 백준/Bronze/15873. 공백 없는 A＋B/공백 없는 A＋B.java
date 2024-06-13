import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        if (n % 10 == 0) {
            n /= 100;
            System.out.println(10 + n);
        } else {
            int a = n % 10;
            n /= 10;
            if (n == 10) {
                System.out.println(10 + a);
            } else {
                System.out.println(a + n);
            }
        }
    }
}