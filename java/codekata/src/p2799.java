
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class p2799 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int m=Integer.parseInt(st.nextToken()), n=Integer.parseInt(st.nextToken());
        br.readLine();
        int[] count = {0,0,0,0,0};
        for (int i=0;i<m;i++){
            int[] windows = new int[n];
            for (int j=0;j<n;j++) windows[j]=0;
            for (int l=0;l<4;l++) {
                String line = br.readLine();
                for (int j=0;j<n;j++){
                    if (line.charAt(j*5+1)=='*') windows[j]+=1;
                }
            }
            br.readLine();
            for (int j=0;j<n;j++){
                count[windows[j]]+=1;
            }
        }
        for (int i=0;i<5;i++){
            System.out.print(count[i]+" ");
        }
    }
}
