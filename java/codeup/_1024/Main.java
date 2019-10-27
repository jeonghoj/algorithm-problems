package _1024;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String input = sc.next();
        for (int i = 0; i < input.length(); i++) {
            char temp = input.charAt(i);
            if(temp != ' '){
                System.out.print("\'"+temp+"\'");
            }else break;
            System.out.print("\n");
        }
    }
}