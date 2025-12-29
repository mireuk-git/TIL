
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class p2998 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        String b = st.nextToken();
        b = "0".repeat(3-b.length()%3) + b;
        String o = "";
        for (int i=0;i<b.length();i+=3){
            int tmp = 0;
            for (int j=0;j<3;j++){
                tmp*=2;
                tmp+=Character.getNumericValue(b.charAt(i+j));
            }
            o+=tmp;
        }
        if (o.charAt(0)=='0') System.out.println(o.substring(1));
        else System.out.println(o);
    }
}
