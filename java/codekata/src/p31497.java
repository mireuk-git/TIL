
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class p31497 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        String[] names = new String[n];
        for (int i=0;i<n;i++){
            st = new StringTokenizer(br.readLine());
            names[i] = st.nextToken();
        }
        int lie = 0;
        for (int i=0;i<n;i++) {
            int resSum=0;
            for (int j=0;j<2;j++){
                System.out.println("? "+names[i]);
                System.out.flush();
                st = new StringTokenizer(br.readLine());
                resSum+=Integer.parseInt(st.nextToken());
            }
            if (resSum==1) lie = i+1;
            else if (resSum==2){
                lie = 0;
                System.out.println("! "+names[i]);
                System.out.flush();
                break;
            }
        }
        
        if (lie>0){
            System.out.println("! "+names[lie-1]);
            System.out.flush();
        }
    }
}
