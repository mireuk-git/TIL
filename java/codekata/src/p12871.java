
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class p12871 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        String s = st.nextToken();
        st = new StringTokenizer(br.readLine());
        String t = st.nextToken();
        if (s.length()>t.length()){
            String tmp = s;
            s = t; t = tmp; 
        }
        int a = t.length(), b = s.length();
        while (b > 0){
            int tmp = a;
            a=b; b=tmp%b;
        }
        int tLength=t.length(), sLength=s.length();
        s=s.repeat(tLength/a); t=t.repeat(sLength/a);
        if (s.equals(t)){ System.out.println(1); }
        else { System.out.println(0); }
    }
}