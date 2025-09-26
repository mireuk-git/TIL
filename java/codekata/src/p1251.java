
import java.io.BufferedInputStream;
import java.io.IOException;
import java.util.HashSet;
import java.util.Set;
import java.util.StringTokenizer;

public class p1251{
    public static void main(String[] args) throws IOException {
        BufferedInputStream br = new BufferedInputStream(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        String s = st.nextToken();
        int l = s.length();
        Set<String> set = new HashSet<>();
        for (int idx1=0;idx1<l-2;idx1++){
            String r = String.valueOf(s.charAt(idx1));
            for (int i=idx1;i>=0;i++) r+=String.valueOf(s.charAt(i));
            for (int idx2=idx1+1;idx2<l-1;idx2++){
                String rTmp = r;
                
            }
        }
    }
}