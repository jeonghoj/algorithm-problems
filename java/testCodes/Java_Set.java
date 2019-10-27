import java.util.*;

public class Java_Set {



}

class location{
    private final int x;
    private final int y;
    location(int x, int y){
        if(x <= y){
            this.x = x;
            this.y = y;
        }else {
            this.x = y;
            this.y = x;
        }
    }
}
