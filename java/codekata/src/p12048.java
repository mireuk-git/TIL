import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class p12048 {
    public static void main(String[] args)throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int t = Integer.parseInt(st.nextToken());

        for (int testCase=1;testCase<=t;testCase++){
            System.out.println("Case #"+testCase+":");
            st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());
            int q = Integer.parseInt(st.nextToken());
            int[] initial = new int[n];

            st = new StringTokenizer(br.readLine());
            for (int i=0;i<n;i++){ initial[i] = Integer.parseInt(st.nextToken()); }

            List<Long> second = new ArrayList<>();
            long[] prefix = new long[n+1];
            for (int i=0;i<n;i++) prefix[i+1] = prefix[i] + initial[i];
            for (int i=0;i<n;i++){
                for (int j=i;j<n;j++) second.add(prefix[j+1]-prefix[i]);
            }
            second.sort(null);

            for (int i=0;i<q;i++){
                st = new StringTokenizer(br.readLine());
                int l = Integer.parseInt(st.nextToken());
                int r = Integer.parseInt(st.nextToken());
                long sum = 0;
                for (int j=l-1;j<r;j++) sum+=second.get(j); 
                System.out.println(sum);
            }
        }
    }
}