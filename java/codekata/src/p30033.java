
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class p30033 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] a = new int[n];
        for (int i=0;i<n;i++) a[i] = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());
        int[] b = new int[n];
        for (int i=0;i<n;i++) b[i] = Integer.parseInt(st.nextToken());
        int count=0;
        for (int i=0;i<n;i++) {
            if (a[i]<=b[i]) count++;
        }
        System.out.println(count);
    }
}
