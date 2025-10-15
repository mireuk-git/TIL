
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class p32855 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        String a = st.nextToken();
        st=new StringTokenizer(br.readLine());
        String b = st.nextToken();

        String[] tmp = a.split("\\.");
        int aInt = Integer.parseInt(tmp[0]), aDeci = Integer.parseInt(tmp[1]);
        tmp = b.split("\\.");
        int bInt = Integer.parseInt(tmp[0]), bDeci = Integer.parseInt(tmp[1]);

        int intTuple;
        if (aInt > bInt){ intTuple = 1; }
        else if (aInt < bInt){ intTuple = -1; }
        else {
            if (aDeci > bDeci){ intTuple = 1; }
            else if (aDeci < bDeci){ intTuple = -1; }
            else { intTuple = 0; }
        }

        int deci; double returnValue;
        double aFloat = Double.parseDouble(a);
        double bFloat = Double.parseDouble(b);
        if (aFloat > bFloat) { deci = 1; returnValue = aFloat; }
        else if (aFloat < bFloat){ deci = -1; returnValue = bFloat; }
        else{ deci = 0; returnValue = aFloat; }

        if (deci==intTuple){ System.out.println(returnValue); }
        else {System.out.println(-1); }
    }
}
