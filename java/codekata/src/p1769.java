
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class p1769 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        String input = st.nextToken();

        int cnt = 1;
        int nextX = 0;
        for (int i=0;i<input.length();i++){
            nextX += (int)input.charAt(i) - 48;
        }
        if (input.length()==1) cnt-=1;
        int x = nextX;

        while (x>9){
            nextX=0;
            while (x>0){
                nextX+=x%10;
                x/=10;
            }
            cnt+=1;
            x=nextX;
        }
        System.out.println(cnt);
        if (x%3==0) System.out.println("YES");
        else System.out.println("NO");
    }
}
