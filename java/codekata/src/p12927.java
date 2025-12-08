
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class p12927 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        String feed = st.nextToken();
        int n = feed.length();
        boolean[] status = new boolean[n+1];
        for (int i=1;i<=n;i++){
            if (feed.charAt(i-1) == 'Y') status[i]=true;
            else if (feed.charAt(i-1) == 'N') status[i]=false;
        }

        int cnt = 0;
        for (int i=1;i<=n;i++){
            if (status[i]) {
                for (int j=i;j<=n;j+=i) status[j] = !status[j];
                cnt++;
            }
        }
        System.out.println(cnt);
    }
}
