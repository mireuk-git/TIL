
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.StringTokenizer;

public class p23746{
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        HashMap<Character,String> decode = new HashMap<>();
        HashMap<Character,Integer> length = new HashMap<>();
        for (int i=0;i<n;i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            String v = st.nextToken();
            char k = st.nextToken().charAt(0);
            decode.put(k,v);
            length.put(k,v.length());
        }
        String compressed = br.readLine();
        StringTokenizer st = new StringTokenizer(br.readLine());
        int s = Integer.parseInt(st.nextToken());
        int e = Integer.parseInt(st.nextToken());
        int i = 0;
        int left = 0, right = 0;
        while ( left+length.get(compressed.charAt(i))<s ){
            left+=length.get(compressed.charAt(i));
            i++;
        }
        right = left;
        String decoded = "";
        while( right+length.get(compressed.charAt(i))<e ){
            decoded = decoded.concat(decode.get(compressed.charAt(i)));
            right+=length.get(compressed.charAt(i));
            i++;
        }
        decoded = decoded.concat(decode.get(compressed.charAt(i)));
        System.out.println(decoded.substring(s-left-1,e-left));
    }
}