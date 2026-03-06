
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class p32046 {
    public static void main(String args[]) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int sum;
        while (n>0){
            sum = 0;
            st = new StringTokenizer(br.readLine());
            for (int i=0;i<n;i++){
                int a = Integer.parseInt(st.nextToken());
                if (sum+a<=300) sum+=a;
            }
            System.out.println(sum);
            st = new StringTokenizer(br.readLine());
            n = Integer.parseInt(st.nextToken());
        }
    }
}
