
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.StringTokenizer;

public class p6147 {
    public static void main(String[] args)throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());
        List<Integer> h = new ArrayList<>();
        for (int i=0;i<n;i++){
            st = new StringTokenizer(br.readLine());
            h.add(Integer.parseInt(st.nextToken()));
        }
        h.sort(Comparator.reverseOrder());
        
        int s = 0;
        int cnt = 0;
        while (s<b){
            s+=h.get(cnt);
            cnt+=1;
        }
        System.out.println(cnt);
    }
}
