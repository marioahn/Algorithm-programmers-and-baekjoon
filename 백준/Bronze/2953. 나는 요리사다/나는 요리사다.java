import java.util.Scanner;

public class Main {

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		int[][] arr = new int[5][4];

		int score = 0; // 평가 점수 합
		int max = 0; // 가장 큰 점수
		int who = 0; // 몇 번째 참가자인지
		// 2차원 배열에 값 넣어주기
		for (int i = 0; i < arr.length; i++) {
			for (int j = 0; j < arr[i].length; j++) {
				arr[i][j] = sc.nextInt();
				score += arr[i][j];

			}
			// 가장 높은 점수
			if (max < score) {
				max = score;
				who = i + 1;
			}
			score = 0;
		}

		System.out.println(who + " " + max);
		sc.close();
	}
}