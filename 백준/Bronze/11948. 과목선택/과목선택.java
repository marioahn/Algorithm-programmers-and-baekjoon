import java.util.Arrays;
import java.util.Collections;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);

		int[] science = new int[4];
		// 과학점수들 입력받기
		for (int i = 0; i < science.length; i++) {
			science[i] = sc.nextInt();
		}
		// 사회탐구 점수
		int E = sc.nextInt();
		int F = sc.nextInt();
		sc.close();

		// 오름차순으로 정렬하기
		Arrays.sort(science);

		// 과학점수 중 높은 과목 3개 합
		int sumA = 0;
		for (int i = science.length - 1; i > 0; i--) {
			sumA += science[i];
		}
		System.out.println(sumA + Math.max(E, F));

	}
}