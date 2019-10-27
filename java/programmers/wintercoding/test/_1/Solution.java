package wintercoding.test._1;

import java.math.BigInteger;

public class Solution {
    public long solution(int w,int h) {
        long answer = 1;
        return answer;
    }

    public static void main(String[] args) {
        int w = 8;
        int h = 12;
        BigInteger big = new BigInteger(String.valueOf(w*h));
        big = big.subtract(BigInteger.valueOf(w+h-gcd(w,h)));
        long answer = big.longValue();


        System.out.println(answer);

        System.out.println( gcd(12,21) ); // 3
        System.out.println( gcd(20,8) ); // 4


    }

    private static int gcd(int a, int b) {
        return BigInteger .valueOf(a).gcd(BigInteger .valueOf(b)).intValue();
    }
}
