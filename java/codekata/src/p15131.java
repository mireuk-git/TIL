
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class p15131 {
    public static void main(String[] args)throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int sum = n/3*7;
        n %= 3;
        switch (n){
            case 0:
                break;
            case 1:
                sum-=3;
                break;
            case 2: 
                sum+=1;
                break;
        }
        System.out.println(sum);
    }
}
