package wintercoding.test._2_giveup;

// 정올 문제
// http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=1862&sca=50&sfl=wr_hit&stx=2601&sop=and

import java.util.Arrays;

class Solution {
    public int[] solution(int n) {
        int[] answer = {};
        return answer;
    }

    public static void main(String[] args) {

        // 2
        // 001
        // 100

        // 4
        // 001001110011011

        // 0000000 0 0000000
        // 0000000 0 1111111

        // 000 0 000 0 111 1 111
        // 001 0 110 0 110 1 001


        // 001 0 011 0 001 1 011

        // 110110011100100
        int n = 2;
        int length = (int) Math.pow(2,n)-1;
        int[] answer = new int[length];


//        for(int i=0; i<n;i++){
//            flip(answer);
//        }
        flip(answer);
        for (int i = 0; i < length; i++) {
            System.out.print(answer[i]+" ");
        }
        System.out.println();

        flip(answer);

        for (int i = 0; i < length; i++) {
            System.out.print(answer[i]+" ");
        }
    }

    public static void flip(int[] arr){
        int length = arr.length;
        System.out.println(length);
        if(length == 3){
            arr[length-1]=1-arr[length-1];
        }else {
            flip(Arrays.copyOfRange(arr,0,length/2));
            for(int i=length/2+1 ; i<length;i++){
                arr[i]= 1-arr[i];
            }
            flip(Arrays.copyOfRange(arr,length/2+1,length));
        }
    }
}
