
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class p11576 {
    public static void main(String[] args)throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int a = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        int m = Integer.parseInt(st.nextToken());
        int deci = 0;
        st = new StringTokenizer(br.readLine());
        for (int i=0;i<m;i++) {
            deci*=a;
            deci += Integer.parseInt(st.nextToken());
        }

        List<Integer> r = new ArrayList<>();
        while(deci>0){
            r.add(deci%b);
            deci/=b;
        }
        
        for (int i=r.size()-1;i>=0;i--) System.out.print(r.get(i)+" ");
    }
}
