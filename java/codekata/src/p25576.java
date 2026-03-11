
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class p25576{
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int[] l = new int[m];
        st = new StringTokenizer(br.readLine());
        for (int j=0;j<m;j++) l[j]=Integer.parseInt(st.nextToken());
        int count=0;
        for (int i=1;i<n;i++){
            int diffsum = 0;
            st = new StringTokenizer(br.readLine());
            for (int j=0;j<m;j++){
                int k = Integer.parseInt(st.nextToken());
                diffsum+=Math.abs(l[j]-k);
            }
            if (diffsum>2000) count++;
        }
        if (count>=n/2) System.out.println("YES");
        else System.out.println("NO");
    }
}