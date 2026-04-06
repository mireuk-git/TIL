
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
/*
public class p13877{
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        for (int test=1;test<=t;test++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            st.nextToken();
            int n = Integer.parseInt(st.nextToken());
            int d = n;
            int o = 0, h = 0;
            int i=0;
            while(n>0){
                if (o>=0 && n%10<8) o+=(n%10)*Math.pow(8, i);
                else o=-1;
                h+=(n%10)*Math.pow(16,i);
                n/=10;
                i++;
            }
            if (o<0) o=0;
            System.out.println(test+" "+o+" "+d+" "+h);
        }
    }
}
*/

public class p13877{
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        for (int i=0;i<t;i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            int k = Integer.parseInt(st.nextToken());
            String s = st.nextToken();

            int oct = 0;
            boolean validOct = true;
            for (char c: s.toCharArray()){
                if (c=='8'||c=='9'){
                    validOct = false;
                    break;
                }
            }
            if (validOct) oct = Integer.parseInt(s,8);
            
            int dec = Integer.parseInt(s,10);
            int hex = Integer.parseInt(s,16);
            System.out.println(k+" "+oct+" "+dec+" "+hex);
        }
    }
}