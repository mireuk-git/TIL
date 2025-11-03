
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class p30189 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int small, big;
        if (n<m) { small = n; big = m; }
        else { small = m; big = n; }

        int cnt = 0;
        for (int i=0;i<=small;i++){ cnt+=i+1; }
        for (int i=small+1;i<=big;i++){ cnt+=small+1; }
        for (int i=big+1;i<=big+small;i++){ cnt+=small+1-i+big; }
        System.out.println(cnt);
    }
}
