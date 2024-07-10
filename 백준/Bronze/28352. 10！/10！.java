import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main extends Exception {
    public static void main(String[] args) throws IOException {
        // 팩토리얼을 계산한 뒤, 24*60*60으로 나눈다

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        long num = Long.parseLong(br.readLine());
        long numFac = 1;

        for (int i = 1; i <= num; i++) {
            numFac *= i;
        }

        long answer = numFac / (7*24*60*60);

        sb.append(answer);
        System.out.println(sb.toString());
    }
}