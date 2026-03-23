import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class p33557 {
    public static void main(String[] args)throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        for (int i=0;i<t;i++){ // t번 반복
            // 입력
            StringTokenizer st = new StringTokenizer(br.readLine());
            String aString = st.nextToken();
            long a = Integer.parseInt(aString);
            String bString = st.nextToken();
            long b = Integer.parseInt(bString);

            // 더 짧은 수 보정
            if (aString.length()<bString.length()){
                aString = "1".repeat(bString.length()-aString.length()).concat(aString);
            }
            else{
                bString = "1".repeat(aString.length()-bString.length()).concat(bString);
            }

            // 각 자리마다 곱셈, 문자열로 concat
            String cal = "";
            for (int j=0;j<aString.length();j++){
                cal+=(aString.charAt(j)-'0')*(bString.charAt(j)-'0');
            }
            // 비교 후 출력
            if (Long.parseLong(cal)==a*b) System.out.println(1);
            else System.out.println(0);
        }
    }
}
