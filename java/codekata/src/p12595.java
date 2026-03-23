
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.StringTokenizer;

public class p12595 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        for (int t=1;t<=n;t++){
            int g = Integer.parseInt(br.readLine());
            HashSet<String> s = new HashSet<>();
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j=0;j<g;j++){
                String c = st.nextToken();
                if (s.contains(c)) s.remove(c);
                else s.add(c);
            }
            System.out.println("Case #"+t+": "+s.iterator().next());
        }
    }
}
