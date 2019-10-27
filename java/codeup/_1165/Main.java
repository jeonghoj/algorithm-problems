package _1165;

        import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int time = sc.nextInt();

        int score = sc.nextInt();

        final int FINAL_TIME = 89;

        int result = ((FINAL_TIME - time) / 5 + 1) + score;

        System.out.print(result);
    }

}
