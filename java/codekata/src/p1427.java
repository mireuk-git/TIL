
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.StringTokenizer;

public class p1427 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader((new InputStreamReader(System.in)));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        List<Integer> separated = new ArrayList<>();
        while(n>0){
            separated.add(n%10);
            n/=10;
        }
        separated.sort(Comparator.reverseOrder());
        for (int i=0;i<separated.size();i++){
            System.out.print(separated.get(i));
        }
    }
}
