
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class p20355 {
    public static void main(String[] args)throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String w = br.readLine();
        int count=0;
        for (int i=0;i<26;i++){
            boolean flag=true;
            for (char c:w.toCharArray()){
                if ((c+i)%26==1) {
                    flag=false;
                    break;
                }
            }
            if (flag) count++;
        }
        if (count==0) System.out.println("impossible");
        else System.out.println(count);
    }
}
