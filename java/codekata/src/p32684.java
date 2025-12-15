
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class p32684 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] p1 = new int[6];
        for (int i=0;i<6;i++) p1[i] = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());
        int[] p2 = new int[6];
        for (int i=0;i<6;i++) p2[i] = Integer.parseInt(st.nextToken());
        double p1Score = p1[0]*13 + p1[1]*7 + p1[2]*5 + p1[3]*3 + p1[4]*3 + p1[5]*2;
        double p2Score = p2[0]*13 + p2[1]*7 + p2[2]*5 + p2[3]*3 + p2[4]*3 + p2[5]*2 + 1.5;
        if (p1Score > p2Score) System.out.println("cocjr0208");
        else System.out.println("ekwoo");
    }
}