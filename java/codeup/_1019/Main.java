package _1019;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String date = sc.nextLine();
        String[] date_arr = date.split("\\.");
        if(date_arr.length==3){
            int year = Integer.parseInt(date_arr[0]);
            int month = Integer.parseInt(date_arr[1]);
            int day = Integer.parseInt(date_arr[2]);
            System.out.printf("%04d.%02d.%02d",year,month,day);
        } else {
            System.out.println("not vaild");
        }

    }
}