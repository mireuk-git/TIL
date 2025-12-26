
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class p21771{
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        StringTokenizer st = new StringTokenizer(br.readLine());
        int r = Integer.parseInt(st.nextToken()), c = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());
        int rg = Integer.parseInt(st.nextToken()), cg = Integer.parseInt(st.nextToken());
        int rp = Integer.parseInt(st.nextToken()), cp = Integer.parseInt(st.nextToken());
        int countR=0;
        boolean onPillow = true;
        for (int i=0;i<r;i++){
            st = new StringTokenizer(br.readLine());
            String s = st.nextToken();
            int countC=0;
            for (int j=0;j<c;j++){
                if (s.charAt(j)=='P') countC++;
            }
            if (countC>=cp) countR++;
        }
        if (countR>=rp) onPillow = false;
        if (onPillow) System.out.println(1);
        else System.out.println(0);
    }
}