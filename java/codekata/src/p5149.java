
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class p5149 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int k = Integer.parseInt(st.nextToken());
        for (int dataSet=1;dataSet<=k;dataSet++){
            st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());
            int m = Integer.parseInt(st.nextToken());
            int [][] coords = new int[n][2];
            for (int i=0;i<n;i++){
                st = new StringTokenizer(br.readLine());
                coords[i][0] = Integer.parseInt(st.nextToken());
                coords[i][1] = Integer.parseInt(st.nextToken());
            }
            int[] order = new int[m];
            st = new StringTokenizer(br.readLine());
            for (int i=0;i<m;i++) order[i] = Integer.parseInt(st.nextToken());

            int maxX=Integer.MIN_VALUE,maxY=Integer.MIN_VALUE,minX=Integer.MAX_VALUE,minY=Integer.MAX_VALUE;
            for (int i=0;i<m;i++){
                if (coords[order[i]-1][0] > maxX) maxX=coords[order[i]-1][0];
                if (coords[order[i]-1][0] < minX) minX=coords[order[i]-1][0];
                if (coords[order[i]-1][1] > maxY) maxY=coords[order[i]-1][1];
                if (coords[order[i]-1][1] < minY) minY=coords[order[i]-1][1];
            }
            int cnt = 0;
            for (int i=0;i<n;i++){
                if (minX<=coords[i][0] && coords[i][0]<=maxX && minY<=coords[i][1] && coords[i][1]<=maxY) cnt++;
            }
            System.out.printf("Data Set %d:\n%d\n\n",dataSet,cnt);

        }
    }
}
