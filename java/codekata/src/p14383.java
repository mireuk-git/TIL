
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class p14383 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int t = Integer.parseInt(st.nextToken());
        for (int testCase = 1; testCase <= t; testCase++ ){
            st = new StringTokenizer(br.readLine());
            String s = st.nextToken();
            int length = s.length(), count = 0;
            for (int i = 0; i < length-1; i++){
                if (s.charAt(i) != s.charAt(i+1)){
                    count++;
                    if (s.charAt(i) == '-') s = "+".repeat(i+1)+s.substring(i+1,length);
                    else s = "-".repeat(i+1)+s.substring(i+1,length);
                }
            }
            if (s.charAt(0)=='-') count++;
            System.out.println("Case #"+testCase+": "+count);
        }
    }
}
