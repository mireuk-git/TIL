
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

class Candidate{
    int id;
    int[] count = {0,0,0,0};
    int score = 0;

    Candidate(int id){
        this.id = id;
    }
}

public class p2456{
    public static void main(String args[])throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader((System.in)));
        int n = Integer.parseInt(br.readLine());
        List<Candidate> c = new ArrayList<>();
        for (int i=1;i<=3;i++) c.add(new Candidate(i));
        for (int idx = 0; idx < n; idx++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j=0;j<3;j++){
                int s = Integer.parseInt(st.nextToken());
                c.get(j).count[s]++;
                c.get(j).score+=s;
            }
        }
        c.sort((p1,p2) -> {
            if (p1.score != p2.score) return Integer.compare(-p1.score, -p2.score);
            if (p1.count[3] != p2.count[3]) return Integer.compare(-p1.count[3], -p2.count[3]);
            return Integer.compare(-p1.count[2],-p2.count[2]);
        });
        if (c.get(0).count[3] == c.get(1).count[3] && c.get(0).count[2] == c.get(1).count[2]) System.out.print(0+" ");
        else System.out.println(c.get(0).id+" ");
        System.out.println(c.get(0).score);
    }
}