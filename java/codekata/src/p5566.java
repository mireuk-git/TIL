import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class p5566 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken()), m = Integer.parseInt(st.nextToken());
        int[] x = new int[n];
        for (int i=0;i<n;i++) {
            st = new StringTokenizer(br.readLine());
            x[i] = Integer.parseInt(st.nextToken());
        }
        int cnt = 0, z = 0;
        int[] dice = new int[m];
        for (int  j=0; j<m; j++){
            st = new StringTokenizer(br.readLine());
            dice[j] = Integer.parseInt(st.nextToken());
        }

        for (int j=0; j<m; j++){
            cnt++;
            z+=dice[j];
            if (z<n) z+=x[z];
            if (z<0) z=0;
            if (z>=n-1) break;
        }
        System.out.println(cnt);
    }
}
