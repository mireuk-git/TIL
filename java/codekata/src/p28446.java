
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.StringTokenizer;

class locationManager{
    private final HashMap<Integer,Integer> location = new HashMap<>();
    
    public void register(int x, int w){
        location.put(w,x);
    }

    public int getLocation(int w){
        return location.get(w);
    }
}

public class p28446{
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        int m = Integer.parseInt(st.nextToken());
        HashMap<Integer,Integer> location = new HashMap<>();
        int op,x,w;
        for (int i=0;i<m;i++){
            st = new StringTokenizer(br.readLine());
            op = Integer.parseInt(st.nextToken());
            switch (op) {
                case 1: 
                    x = Integer.parseInt(st.nextToken()); 
                    w = Integer.parseInt(st.nextToken());
                    location.put(w,x);
                    break;
                case 2:
                    w = Integer.parseInt(st.nextToken());
                    System.out.println(location.get(w));
                    break;
            }
        }
    }
}