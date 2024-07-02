import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int d = Integer.parseInt(st.nextToken());

            int[] coin = new int[d];
            for (int j = 0; j < d; j++) {
                coin[j] = Integer.parseInt(st.nextToken());
            }

            boolean flag = true;
            System.out.printf("Denominations: %d ", coin[0]);
            for (int j = 1; j < d; j++) {
                if (coin[j - 1] * 2 > coin[j]) {
                    flag = false;
                }
                System.out.printf("%d ", coin[j]);
            }
            System.out.println();

            if (flag) {
                System.out.println("Good coin denominations!");
            } else {
                System.out.println("Bad coin denominations!");
            }
            System.out.println();
        }
    }
}