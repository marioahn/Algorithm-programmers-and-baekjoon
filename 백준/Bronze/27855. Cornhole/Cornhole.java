import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int h1 = Integer.parseInt(st.nextToken());
        int b1 = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        int h2 = Integer.parseInt(st.nextToken());
        int b2 = Integer.parseInt(st.nextToken());

        int p1Score = 3 * h1 + b1;
        int p2Score = 3 * h2 + b2;

        String s = "NO SCORE";
        if (p1Score > p2Score) {
            s = "1 " + (p1Score - p2Score);
        } else if (p2Score > p1Score) {
            s = "2 " + (p2Score - p1Score);
        }

        System.out.printf(s);
    }
}