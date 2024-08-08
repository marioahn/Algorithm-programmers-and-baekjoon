import java.util.Scanner;
 
public class Main {
    public static void main(String args[]) {
        
        Scanner sc = new Scanner(System.in);
        
        int a = 0;
        String trans = "";
        int b = 0;
        
        while (true) {
            a = sc.nextInt();
            trans = sc.next();
            b = sc.nextInt();
            
            if (a == 0 && trans.equals("W") && b == 0) break;
            
            if (trans.equals("D")) {
                System.out.println(a + b);
            }
            else {
                if (a - b < -200) {
                    System.out.println("Not allowed");
                }
                else {
                    System.out.println(a - b);
                }
            }
        }
 
    }
}