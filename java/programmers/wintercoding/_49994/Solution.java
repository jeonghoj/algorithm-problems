package wintercoding._49994;

import java.util.Iterator;
import java.util.Vector;

public class Solution {
    public int solution(String dirs) {
        int answer = 0;
        int x = 0;
        int y = 0;
        Vector<Moved> mv = new Vector<>();

        for(int i = 0; i<dirs.length(); i++){
            boolean overMoved = false;
            LocationXY from = new LocationXY(x,y);
            switch (dirs.charAt(i)){
                case 'U':
                    if(y == 5){
                        overMoved = true;
                        break;
                    }
                    y+=1;
                case 'D':
                    if(y == -5){
                        overMoved = true;
                        break;
                    }
                    y+=1;
                case 'L':
                    if(x == -5){
                        overMoved = true;
                        break;
                    }
                    x-=1;
                case 'R':
                    if(x == 5){
                        overMoved = true;
                        break;
                    }
                    x+=1;
            }
            if(!overMoved){
                LocationXY to = new LocationXY(x,y);
                Moved temp = new Moved(from,to);
                boolean alreadyMoved = false;
                Iterator<Moved> itr = mv.iterator();
                while (itr.hasNext()){
                    if(temp.equals(itr.next())){
                        alreadyMoved = true;
                        break;
                    }
                }
                if(!alreadyMoved){
                    mv.add(new Moved(from,to));
                }
            }
        }
        answer = mv.size();
        return answer;
    }

    public static void main(String[] args) {
        LocationXY l1 = new LocationXY(2,1);
        LocationXY l2 = new LocationXY(3,1);
        LocationXY l3 = new LocationXY(3,1);
        LocationXY l4 = new LocationXY(2,1);
        Moved[] mvs = new Moved[5];
        mvs[0] = new Moved(l1,l2);
        mvs[1] = new Moved(l3,l4);
        System.out.println(l1.equals(l2));
        System.out.println(l1.equals(l3));
        System.out.println(mvs[0].equals(mvs[1]));
        System.out.println(l1.hashCode());
        System.out.println(l2.hashCode());
        System.out.println(l3.hashCode());
        System.out.println(l4.hashCode());
        System.out.println(mvs[0].hashCode());
        System.out.println(mvs[1].hashCode());


    }

//    public static void main(String[] args) {
//        String dirs = "LR";
//
//        int answer = 0;
//
//        int x = 0;
//        int y = 0;
//        Vector<Moved> mv = new Vector<>();
//
//        for(int i = 0; i<dirs.length(); i++){
//            boolean overMoved = false;
//            LocationXY from = new LocationXY(x,y);
//            System.out.println(dirs.charAt(i));
//            switch (dirs.charAt(i)){
//                case 'U':
//                    if(y == 5){
//                        overMoved = true;
//                        break;
//                    }
//                    y+=1;
//                    break;
//                case 'D':
//                    if(y == -5){
//                        overMoved = true;
//                        break;
//                    }
//                    y-=1;
//                    break;
//                case 'L':
//                    if(x == -5){
//                        overMoved = true;
//                        break;
//                    }
//                    x-=1;
//                    break;
//                case 'R':
//                    if(x == 5){
//                        overMoved = true;
//                        break;
//                    }
//                    x+=1;
//                    break;
//            }
//            System.out.printf("%d, %d\n", x,y);
//            System.out.println(overMoved);
//            if(!overMoved){
//                LocationXY to = new LocationXY(x,y);
//                Moved temp = new Moved(from,to);
//                boolean alreadyMoved = false;
//                Iterator<Moved> itr = mv.iterator();
//                while (itr.hasNext()){
//                    if(temp.equals(itr.next())){
//                        alreadyMoved = true;
//                        break;
//                    }
//                }
//                if(!alreadyMoved){
//                    mv.add(new Moved(from,to));
//                }
//            }
//        }
//        answer = mv.size();
//
//        System.out.println(answer);
//    }
}


class LocationXY {
    int x;
    int y;
    LocationXY(int x, int y){
        this.x = x;
        this.y = y;
    }

    boolean equals(LocationXY l) {
        return this.x == l.x && this.y == l.y;
    }
}

class Moved {
    LocationXY l1;
    LocationXY l2;
    Moved(LocationXY l1,LocationXY l2){
        //1 1 1 2 1 2 1 1
        //1 1 1 2 1 2 1 1
        //1 1 2 1 2 1 1 1
        if(l1.x <= l2.x){
            if(l1.y <= l2.y){
                this.l1 = l1;
                this.l2 = l2;
            }else {
                this.l1 = l2;
                this.l2 = l1;
            }
        }else {
            this.l1 = l2;
            this.l2 = l1;
        }
    }
    boolean equals(Moved m) {
        return this.l1.x == m.l1.x && this.l1.y == m.l1.y && this.l2.x == m.l2.x && this.l2.y == m.l2.y;
    }

    @Override
    public int hashCode() {
        int hash = 7;

        // 1 1 1 2
        // 1 2 1 1

        hash = 31 * hash + l1.x*3 + l1.y*3 + l2.x*17 + l2.y*17;
        return hash;
    }
}


