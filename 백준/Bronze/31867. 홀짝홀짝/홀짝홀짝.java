import java.io.*;
import java.util.*;

public class Main {
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int n = Integer.parseInt(br.readLine()); // 자릿수
		char[] arr = br.readLine().toCharArray(); // 자연수
		
		int even = 0; // 짝수의 개수
		int odd = 0; // 홀수의 개수
		
		int num;
		for (int i = 0; i < n; i++) {
			num = arr[i] - '0';
			
			if (num % 2 == 0) { // 짝수이면
				even++;
			} else { // 홀수이면
				odd++;
			}
		}
		
		int result = -1;
		if (even > odd) { // 짝수가 많다면
			result = 0;
		} else if (even < odd) { // 홀수가 많다면
			result = 1;
		}
		
		bw.write(Integer.toString(result));
		bw.flush();
		bw.close();
		br.close();
	}
}