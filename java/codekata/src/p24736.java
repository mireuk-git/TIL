
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class p24736 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader((System.in)));
        String output = "";
        for (int i=0;i<2;i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            int s=0;
            s+=6*Integer.parseInt(st.nextToken());
            s+=3*Integer.parseInt(st.nextToken());
            s+=2*Integer.parseInt(st.nextToken());
            s+=1*Integer.parseInt(st.nextToken());
            s+=2*Integer.parseInt(st.nextToken());
            output+=s+" ";
        }
        System.out.println(output);
    }
}