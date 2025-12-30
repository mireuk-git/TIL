
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;


public class p17252 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int s = n;
        for (int i=19;i>=0;i--){
            if (Math.pow(3,i)<=s){
                s-=Math.pow(3,i);
            }
        }
        if (n!=0 && s==0) System.out.println("YES");
        else System.out.println("NO");
    }
}
