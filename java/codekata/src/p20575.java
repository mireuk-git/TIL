
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class p20575 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int count = 0;
        for (int i=0;i<n;i++){
            st = new StringTokenizer(br.readLine());
            double x1 = Double.parseDouble(st.nextToken()), y1 = Double.parseDouble(st.nextToken());
            double x2 = Double.parseDouble(st.nextToken()), y2 = Double.parseDouble(st.nextToken());
            if (x1>x2) { double tmp = x1; x1=x2; x2=tmp; }
            if (Math.ceil(x1)<x2) { count++; }
        }
        double piApprox = 2.0*n/count;
        System.out.println(piApprox);
    }
}
