
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.StringTokenizer;

public class p11652 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        HashMap<Long,Integer> count = new HashMap<>();
        long max = 0;
        count.put(max,0);
        for (int i=0;i<n;i++){
            st = new StringTokenizer(br.readLine());
            long feed = Long.parseLong(st.nextToken());
            count.put(feed,count.getOrDefault(feed, 0)+1);
            if (count.get(max)<count.get(feed)) max = feed;
            else if (count.get(max).equals(count.get(feed)) && max>feed) max = feed;
        }
        if (10==10) 
        System.out.println(max);
    }
}
