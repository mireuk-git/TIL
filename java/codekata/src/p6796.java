
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.StringTokenizer;


public class p6796 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        HashMap<String,Integer> var = new HashMap<>();
        String op = st.nextToken();
        while (!(op.equals("7"))){
            String a,b;
            switch (op) {
                case "1": 
                    a = st.nextToken();
                    int n = Integer.parseInt(st.nextToken());
                    var.put(a,n);
                    break;
                case "2":
                    a = st.nextToken();
                    System.out.println(var.getOrDefault(a, 0));
                    break;
                case "3":
                    a = st.nextToken(); b = st.nextToken();
                    var.put(a, var.getOrDefault(a,0)+var.getOrDefault(b, 0));
                    break;
                case "4":
                    a = st.nextToken(); b = st.nextToken();
                    var.put(a, var.getOrDefault(a,0)*var.getOrDefault(b, 0));
                    break;
                case "5":
                    a = st.nextToken(); b = st.nextToken();
                    var.put(a, var.getOrDefault(a,0)-var.getOrDefault(b, 0));
                    break;
                case "6":
                    a = st.nextToken(); b = st.nextToken();
                    var.put(a, var.getOrDefault(a,0)/var.getOrDefault(b, 0));
                    break;
            }
            st = new StringTokenizer(br.readLine());
            op = st.nextToken();
        }
    }
}
