import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class p3724 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        for (int testcase=0;testcase<t;testcase++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            int m = Integer.parseInt(st.nextToken());
            int n = Integer.parseInt(st.nextToken());
            long[] mult = new long[m];
            for (int i=0;i<m;i++) mult[i]=1;
            for (int i=0;i<n;i++){
                st = new StringTokenizer(br.readLine());
                for (int j=0;j<m;j++) mult[j] *= Integer.parseInt(st.nextToken());
            }
            long max = 0, maxid = 0;
            for (int i=0;i<m;i++){
                if (maxid==0 || max<mult[i] || (max==mult[i] && maxid<i)) { max = mult[i]; maxid = i;}
            }
            System.out.println(maxid+1);
        }
    }
}
