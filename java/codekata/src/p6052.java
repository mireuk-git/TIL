import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class p6052{
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int s = Integer.parseInt(br.readLine());
        int d1 = s, d2;
        while (true){
            List<Integer> d1Divisor = new ArrayList<>();
            d1Divisor.add(1);
            for (int i=2;i<=Math.sqrt(d1);i++){
                if (d1%i==0){
                    d1Divisor.add(i);
                    d1Divisor.add(d1/i);
                }
            }
            d2=0;
            for (int i: d1Divisor) d2+=i;
            List<Integer> d2Divisor = new ArrayList<>();
            d2Divisor.add(1);
            for (int i=2; i<=Math.sqrt(d2); i++){
                if (d2%i==0){
                    d2Divisor.add(i);
                    d2Divisor.add(d2/i);
                }
            }
            int d2sum = 0;
            for (int i: d2Divisor) d2sum+=i;
            if (d2sum==d1 && d1!=d2) break;
            else d1++;
        }
        System.out.println(d1+" "+d2);
    }
}