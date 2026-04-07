import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class p13155{
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        long r = 1;
        for (int i=0;i<n;i++) r*=8;
        System.out.println(r);
    }
}