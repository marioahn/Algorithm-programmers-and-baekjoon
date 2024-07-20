import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        char[] str = "SciComLove".toCharArray();
        char[] rStr = new char[str.length];
        for (int i = 0; i < str.length; i++) {
            rStr[str.length - 1 - i] = str[i];
        }

        if (n % 2 == 0) {
            System.out.println(str);
        } else {
            System.out.println(rStr);
        }
    }
}