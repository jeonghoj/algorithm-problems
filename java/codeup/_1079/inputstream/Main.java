package _1079.inputstream;

import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) {
        InputStream in = System.in;
        InputStreamReader isr = new InputStreamReader(in);
        try {
            while (true){
                char a = (char) isr.read();
                if(a == ' ') continue;
                System.out.println(a);
                if(a=='q') break;
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
