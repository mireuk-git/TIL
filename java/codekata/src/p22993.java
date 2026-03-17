
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class p22993 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] a = new int[n-1];
        StringTokenizer st = new StringTokenizer(br.readLine());
        long a1 = Long.parseLong(st.nextToken());
        for (int i=0;i<n-1;i++) a[i] = Integer.parseInt(st.nextToken());
        Arrays.sort(a);
        boolean flag = false;
        for (int i:a){
            if (a1>i) a1+=i;
            else {
                flag = true;
                break;
            }
        }
        if (flag) System.out.println("No");
        else System.out.println("Yes");
    }
}
