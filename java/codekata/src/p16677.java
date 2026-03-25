
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

class Word{
    String w;
    int index;
    float g;

    Word(String w, int index, float g){
        this.w = w;
        this.index = index;
        this.g = g;
    }
}

public class p16677 {
    public static void main(String[] args)throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String m = br.readLine();
        int n = Integer.parseInt(br.readLine());
        List<Word> l = new ArrayList<>();
        for (int i=0;i<n;i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            String w = st.nextToken();
            float g = Float.parseFloat(st.nextToken());
            int idx = 0;
            for (char c: w.toCharArray()){
                if (idx>=m.length()) break;
                if (c==m.charAt(idx)) idx++;
            }
            if (idx>=m.length()){
                if (w.length()==m.length()) continue;
                l.add(new Word(w,idx,g/(w.length()-m.length())));
            }
        }
        if (l.isEmpty()) System.out.println("No Jam");
        else{
            l.sort((a,b) -> {
                if (b.g != a.g) return Double.compare(b.g,a.g);
                return Integer.compare(a.index, b.index);
            });
            System.out.println(l.get(0).w);
        }
    }
}
