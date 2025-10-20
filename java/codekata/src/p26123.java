
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class p26123 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken()), d = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());
        int[] h = new int[n];
        int max = 0;
        for (int i = 0; i < n; i++){ 
            h[i] = Integer.parseInt(st.nextToken()); 
            if (h[i] > max) { max = h[i]; }
        }
        max = max-d > 0? max-d : 0;
        long cnt = 0;
        for (int i = 0; i < n; i++){
            if (h[i]>max){
                cnt += h[i] - max;
                h[i] = max;
            }
        }
        System.out.println(cnt);
    }
}
