
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

class IsPrime{
    public static boolean isPrime(long n){
        for(long i=2;i<=Math.sqrt(n);i++){
            if (n%i==0) return false;
        }
        return true;
    }
}
public class p4134 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader((System.in)));
        int t = Integer.parseInt(br.readLine());
        for (int i=0;i<t;i++){
            long n = Long.parseLong(br.readLine());
            if (n<=2) System.out.println(2);
            else {
                long j = n;
                while (!IsPrime.isPrime(j)) j++;
                System.out.println(j);
            }
        }
    }
}
