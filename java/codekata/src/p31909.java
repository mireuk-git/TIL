import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.StringTokenizer;

public class p31909 {
    public static void main(String[] args)throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        HashMap<Integer,Integer> location = new HashMap<>();
        for (int i=0;i<=7;i++) location.put(i,i);

        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());
        for (int i=0;i<n;i++){
            int a = Integer.parseInt(st.nextToken());
            int p1=0,p2=0;
            int count=0;
            for(int j=0;j<=7;j++){
                if (a%2==1){
                    if (++count==1) p1 = j;
                    else if (count==2) p2 = j;
                    else break;
                }
                a/=2;
            }
            if (count!=2) continue;
            int tmp = location.get(p1);
            location.put(p1,location.get(p2));
            location.put(p2,tmp);
        }
        st = new StringTokenizer(br.readLine());
        int k = Integer.parseInt(st.nextToken());
        System.out.println(location.get(k));
    }
}
