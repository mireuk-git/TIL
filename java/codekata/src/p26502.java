
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;

public class p26502 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        Map<Character,Character> crack = new HashMap<>(){{
            put('y','a'); put('a','e'); put('e','i'); put('i','o'); put('o','u'); put('u','y');
            put('Y','A'); put('A','E'); put('E','I'); put('I','O'); put('O','U'); put('U','Y');
        }};
        for (int i=0;i<n;i++){
            String s = br.readLine();
            String replaced = "";
            for (char c: s.toCharArray()){
                if (crack.keySet().contains(c)) replaced+=crack.get(c);
                else replaced+=c;
            }
            System.out.println(replaced);
        }
    }
}
