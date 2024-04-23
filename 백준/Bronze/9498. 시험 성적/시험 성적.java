import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int score = Integer.parseInt(br.readLine());

        br.close();

        String result = "";
        result = (score >= 90) ? "A" : (score >= 80) ? "B" : (score >= 70) ? "C" :
                (score >= 60) ? "D" : "F";
        // 오 이렇게 중.첩 삼항연산자를 이어갈 수도 있네 ㄷㄷㄷ;; 뒤에것들은 elseif고
        // 맨 뒤는 else

        System.out.println(result);


    }
}
