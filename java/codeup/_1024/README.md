```java
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
```

### Comment  

Java 에서 Char을 읽을 떄는 Scanner로 읽어서 String 저장 후 charAt(int index) 함수를 이용하자.

