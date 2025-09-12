import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.StringTokenizer;

public class p18703 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int t = Integer.parseInt(st.nextToken());
        for (int i=0;i<t;i++) {
            st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());
            HashMap<String,Integer> original = new HashMap<>();

            for (int j=0;j<n;j++) {
                st = new StringTokenizer(br.readLine());
                String name = st.nextToken();
                int id = Integer.parseInt(st.nextToken());
                if (id<original.getOrDefault(name,100001)) {
                    original.put(name,id);
                }
            }

            List<Integer> ids = new ArrayList<>(original.values());
            Collections.sort(ids);
            for (int j : ids){
                System.out.print(j+" ");
            }
            System.out.println();
        }
    }
}
