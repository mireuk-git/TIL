
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.StringTokenizer;

public class p28432 {
    public static void main(String[] args)throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        HashSet<String> hash = new HashSet<>();
        String[] s = new String[n];
        int index=0;
        for (int i=0;i<n;i++){
            st = new StringTokenizer(br.readLine());
            String str = st.nextToken();
            if (str.equals("?")) index = i;
            s[i] = str;
            hash.add(str);
        }
        char start,end;
        st = new StringTokenizer(br.readLine());
        int m = Integer.parseInt(st.nextToken());
        String r = "";
        for (int i=0;i<m;i++){
            st = new StringTokenizer(br.readLine());
            String a = st.nextToken();
            boolean startFlag = true, endFlag = true;
            if (index>0){
                start = s[index-1].charAt(s[index-1].length()-1);
                if (a.charAt(0) != start) startFlag = false;
            }
            if (index<n-1){
                end = s[index+1].charAt(0);
                if (a.charAt(a.length()-1)!=end) endFlag = false;
            }
            if (startFlag && endFlag && !hash.contains(a)) r = a;
        }
        System.out.println(r);
    }
}
