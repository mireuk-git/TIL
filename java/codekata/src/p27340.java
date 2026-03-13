
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class p27340{
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());
        int colorcount = 0;
        int tablecount = 0;
        for (int i=0;i<m;i++) {
            int a = Integer.parseInt(st.nextToken());
            if (a>4) {
                colorcount++;
                tablecount += a/4;
            }
        }
        if (tablecount >= n && n >= m && colorcount >= m) System.out.println("DA");
        else System.out.println("NE");
    }
}