import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    int star = scanner.nextInt();

    for(int i = 1; i <= star; i++) {
      for(int j = i; j < star; j++) {
        System.out.print(" ");
      }
      for(int k = 0; k < i*2-1; k++) {
        System.out.print("*");
      }
      System.out.println();
    }
    scanner.close();
  }
}