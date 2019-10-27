package _1097;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        int[][] inputArr = new int[20][20];

        Scanner sc = new Scanner(System.in);

        for (int i = 0; i < 19; i++) {
            for (int j = 0; j < 19; j++) {
                inputArr[i][j] = sc.nextInt();
            }
        }

        int flip_count = sc.nextInt();

        for (int i = 0; i < flip_count; i++) {
            int flip_x = sc.nextInt();
            int flip_y = sc.nextInt();

            // -1을 하는 이유는 실제 좌표가 1부터 시작하기 때문
            flip(inputArr,flip_x-1,flip_y-1);
        }

        for (int i = 0; i < 19; i++) {
            for (int j = 0; j < 19; j++) {
                System.out.print(inputArr[i][j]);
                if(j!=18) System.out.print(" ");
            }
            System.out.print("\n");
        }
    }

    static void flip(int[][] inputArr, int x, int y){
        for (int i = 0; i < 19; i++) {
            if(inputArr[x][i]==0) inputArr[x][i]=1;
            else inputArr[x][i]=0;
        }
        for (int i = 0; i < 19; i++) {
            if(inputArr[i][y]==0) inputArr[i][y]=1;
            else inputArr[i][y]=0;
        }
    }
}
