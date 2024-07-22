import java.io.*;
import java.util.*;

public class Main {
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int a = Integer.parseInt(st.nextToken()); // Division 1 우승 상금
		int p = Integer.parseInt(st.nextToken()); // Division 2 우승 상금
		int c = Integer.parseInt(st.nextToken()); // shake! 우승 상금
		int sum = a + c > p ? a + c : p;
		
		bw.write(Integer.toString(sum));
		bw.flush();
		bw.close();
		br.close();
	}
}