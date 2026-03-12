
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;

public class p11195 {
    public static void main(String[] args)throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String input = br.readLine();
        HashMap<Character,Integer> m = new HashMap<>();
        for (char c: input.toCharArray())m.put(c,m.getOrDefault(c, 0)+1);
        boolean odd = false;
        int count = 0;
        for (char c: m.keySet()){
            System.out.println(c+" "+m.get(c));
            if (m.get(c)%2==1){
                if (!odd) odd = true;
                else count++;
            } 
        }
        System.out.println(count);
    }
}