import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        while (true){
            StringTokenizer st = new StringTokenizer(br.readLine());
            double [] arr = new double[6];

            double sum = 0;
            for(int i=0; i<6; i++){
                arr[i] = Double.parseDouble(st.nextToken());
                sum += arr[i];
            }

            if(sum==0) break;
            Arrays.sort(arr);
            sum -= arr[0] + arr[5];

            if(sum%4 == 0) System.out.printf("%.0f\n", sum/4);
            else System.out.println(sum/4);
        }
    }
}