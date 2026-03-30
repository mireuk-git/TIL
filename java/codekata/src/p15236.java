
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class p15236 {
    public static void main(String[] args)throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int c = 0;
        int spot = 0;
        for (int i=0;i<=n;i++){
            if (i%2==0) c++;
            spot+=i*c;
        }
        for (int i=n+1;i<=2*n;i++){
            if (i%2==1) c--;
            spot+=i*c;
        }
        System.out.println(spot);
    }
}
