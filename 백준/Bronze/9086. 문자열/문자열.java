import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        // 이렇게 문자열을 요소로 가진 배열 만듦!
        String name[] = new String[n];
        for (int i=0; i<n; i++) {
            // 그냥 문자는 next()하면 됨
            String str = sc.next();
            name[i] = str.substring(0,1)+str.substring(str.length()-1,str.length());
        }

        for (int i=0; i<n; i++) {
            System.out.println(name[i]);
        }
    }
}
