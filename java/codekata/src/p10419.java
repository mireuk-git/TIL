
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class p10419 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader((System.in)));
        int t = Integer.parseInt(br.readLine());
        List<Integer> l = new ArrayList<>();
        l.add(0);
        for (int testcase=0;testcase<t;testcase++){
            int d = Integer.parseInt(br.readLine());
            while (d>l.get(l.size()-1)) l.add(l.size()*(l.size()+1));
            for (int i=l.size()-1;i>=0;i--){
                if (l.get(i)<=d){
                    System.out.println(i);
                    break;
                }
            }
        }
    }
}
