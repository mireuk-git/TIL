
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class p15161 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int k = Integer.parseInt(br.readLine());
        int[][] mat = new int[10][10];
        for (int i=0;i<10;i++){
            for (int j=0;j<10;j++) mat[i][j] = k+1;
        }
        for (int w=1;w<=k;w++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int i=0;i<3;i++){
                int r = Integer.parseInt(st.nextToken());
                for (int j=0;j<10;j++) mat[r-1][j] = k+1-w;
            }
            for (int i=0;i<3;i++){
                int c = Integer.parseInt(st.nextToken());
                for (int j=0;j<10;j++) mat[j][c-1] = k+1-w;
            }
        }
        for (int[] i: mat){
            for (int j: i) System.out.print(j+" ");
            System.out.println();
        }
    }
}
