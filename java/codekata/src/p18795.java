
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class p18795 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        long[] a = new long[n];
        long[] b = new long[m];
        st = new StringTokenizer(br.readLine());
        for (int i=0;i<n;i++) { a[i] = Long.parseLong(st.nextToken()); }
        st = new StringTokenizer(br.readLine());
        for (int i=0;i<m;i++) { b[i] = Long.parseLong(st.nextToken()); }

        long trash = 0;
        for (int i=0;i<n;i++) { trash+=a[i]; }
        for (int i=0;i<m;i++) { trash+=b[i]; }
        System.out.println(trash);
    }
}