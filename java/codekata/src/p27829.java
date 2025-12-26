
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.StringTokenizer;

public class p27829 {
    public static void main(String[] args)throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int t = Integer.parseInt(st.nextToken());
        for (int testCase=1;testCase<=t;testCase++){
            br.readLine();
            st = new StringTokenizer(br.readLine());
            int ng = Integer.parseInt(st.nextToken());
            int nm = Integer.parseInt(st.nextToken());

            st = new StringTokenizer(br.readLine());
            List<Integer> g = new ArrayList<>();
            for (int i=0;i<ng;i++) g.add(Integer.parseInt(st.nextToken()));
            st = new StringTokenizer(br.readLine());
            List<Integer> m = new ArrayList<>();
            for (int i=0;i<nm;i++) m.add(Integer.parseInt(st.nextToken()));
            int gi=0,mi=0;
            Collections.sort(g);
            Collections.sort(m);

            while(gi<ng && mi<nm){
                if (g.get(gi) < m.get(mi)) gi++;
                else mi++;
            }

            if (gi>=ng) System.out.println("MechaGodzilla");
            else if (mi>=nm) System.out.println("Godzilla");
            else System.out.println("uncertain");
        }
    }
}
