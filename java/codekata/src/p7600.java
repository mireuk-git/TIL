
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;

public class p7600 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        while (true){
            String input = br.readLine().toLowerCase();
            if (input.equals("#")) break;
            HashSet<Character> s = new HashSet<>();
            for (char c : input.toCharArray()){
                if (c>='a' && c<='z') s.add(c);
            }
            System.out.println(s.size());
        }
    }
}
